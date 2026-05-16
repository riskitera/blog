#!/usr/bin/env python3
"""
gsc-fetch.py — Fetch Google Search Console data for blog.riskitera.com

Guarda metricas diarias en data/gsc-daily/YYYY-MM-DD.json para que
Claude Code las revise al inicio de cada sesion.

Uso:
  python scripts/gsc-fetch.py                    # ultimos 7 dias
  python scripts/gsc-fetch.py --days 28          # ultimos 28 dias
  python scripts/gsc-fetch.py --auth             # re-autenticar (primera vez)

Credenciales: ~/.config/riskitera/gsc/
Site: sc-domain:riskitera.com (o https://blog.riskitera.com/)
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

# Paths
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
DATA_DIR = PROJECT_DIR / "data" / "gsc-daily"
CONFIG_DIR = Path.home() / ".config" / "riskitera" / "gsc"
CLIENT_SECRETS_FILE = CONFIG_DIR / "client_secrets.json"
TOKEN_FILE = CONFIG_DIR / "token.json"

SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]

# Probar ambos formatos de site property
SITE_URLS = [
    "sc-domain:riskitera.com",
    "https://blog.riskitera.com/",
]


def ensure_dirs():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(CONFIG_DIR, 0o700)
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def get_credentials():
    """Obtiene credenciales OAuth, re-autenticando si es necesario."""
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow

    creds = None

    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)

    if creds and creds.valid:
        return creds

    if creds and creds.expired and creds.refresh_token:
        from google.auth.transport.requests import Request
        creds.refresh(Request())
        TOKEN_FILE.write_text(creds.to_json())
        return creds

    # Auth flow
    if not CLIENT_SECRETS_FILE.exists():
        print(f"[ERROR] No existe {CLIENT_SECRETS_FILE}")
        print("Copia el client_secrets.json de ~/.config/riskitera/youtube/ o descargalo de Google Cloud Console.")
        print(f"  cp ~/.config/riskitera/youtube/client_secrets.json {CLIENT_SECRETS_FILE}")
        sys.exit(1)

    import subprocess, webbrowser

    # Registrar Chrome incognito como browser
    class ChromeIncognito(webbrowser.GenericBrowser):
        def open(self, url, new=0, autoraise=True):
            subprocess.Popen([
                "open", "-na", "Google Chrome", "--args", "--incognito", url
            ])
            return True

    webbrowser.register("chrome-incognito", None, ChromeIncognito(""))

    flow = InstalledAppFlow.from_client_secrets_file(str(CLIENT_SECRETS_FILE), SCOPES)
    creds = flow.run_local_server(
        port=8095,
        browser="chrome-incognito",
        open_browser=True,
    )
    TOKEN_FILE.write_text(creds.to_json())
    os.chmod(TOKEN_FILE, 0o600)
    print(f"[OK] Token guardado en {TOKEN_FILE}")
    return creds


def get_service(creds):
    from googleapiclient.discovery import build
    return build("searchconsole", "v1", credentials=creds)


def detect_site_url(service):
    """Detecta el site property correcto."""
    result = service.sites().list().execute()
    sites = result.get("siteEntry", [])

    if not sites:
        print("[ERROR] No tienes sites verificados en Search Console.")
        print("Verifica blog.riskitera.com en https://search.google.com/search-console")
        sys.exit(1)

    print(f"[INFO] Sites disponibles: {[s['siteUrl'] for s in sites]}")

    for url in SITE_URLS:
        for s in sites:
            if s["siteUrl"] == url:
                print(f"[OK] Usando site: {url}")
                return url

    # Fallback: primer site que contenga riskitera
    for s in sites:
        if "riskitera" in s["siteUrl"]:
            print(f"[OK] Usando site (fallback): {s['siteUrl']}")
            return s["siteUrl"]

    print(f"[WARN] No encontre riskitera.com. Usando: {sites[0]['siteUrl']}")
    return sites[0]["siteUrl"]


def fetch_queries(service, site_url, start_date, end_date, row_limit=50):
    """Fetch top queries con metricas."""
    body = {
        "startDate": start_date,
        "endDate": end_date,
        "dimensions": ["query"],
        "rowLimit": row_limit,
        "dataState": "final",
    }
    return service.searchanalytics().query(siteUrl=site_url, body=body).execute()


def fetch_pages(service, site_url, start_date, end_date, row_limit=50):
    """Fetch top pages con metricas."""
    body = {
        "startDate": start_date,
        "endDate": end_date,
        "dimensions": ["page"],
        "rowLimit": row_limit,
        "dataState": "final",
    }
    return service.searchanalytics().query(siteUrl=site_url, body=body).execute()


def fetch_queries_by_page(service, site_url, start_date, end_date, row_limit=100):
    """Fetch queries agrupadas por pagina."""
    body = {
        "startDate": start_date,
        "endDate": end_date,
        "dimensions": ["page", "query"],
        "rowLimit": row_limit,
        "dataState": "final",
    }
    return service.searchanalytics().query(siteUrl=site_url, body=body).execute()


def fetch_daily_totals(service, site_url, start_date, end_date):
    """Fetch totales por dia."""
    body = {
        "startDate": start_date,
        "endDate": end_date,
        "dimensions": ["date"],
        "dataState": "final",
    }
    return service.searchanalytics().query(siteUrl=site_url, body=body).execute()


def format_row(row):
    """Formatea una fila de resultados."""
    return {
        "keys": row["keys"],
        "clicks": row["clicks"],
        "impressions": row["impressions"],
        "ctr": round(row["ctr"] * 100, 2),
        "position": round(row["position"], 1),
    }


def generate_summary(data):
    """Genera resumen legible para Claude."""
    summary = []

    # Totales
    totals = data.get("daily_totals", {}).get("rows", [])
    if totals:
        total_clicks = sum(r["clicks"] for r in totals)
        total_impressions = sum(r["impressions"] for r in totals)
        avg_ctr = (total_clicks / total_impressions * 100) if total_impressions > 0 else 0
        avg_position = sum(r["position"] for r in totals) / len(totals) if totals else 0
        summary.append(f"## Resumen {data['period']['start']} a {data['period']['end']}")
        summary.append(f"- Clicks totales: {total_clicks}")
        summary.append(f"- Impresiones totales: {total_impressions}")
        summary.append(f"- CTR medio: {avg_ctr:.2f}%")
        summary.append(f"- Posicion media: {avg_position:.1f}")
        summary.append("")

    # Top queries
    queries = data.get("top_queries", [])
    if queries:
        summary.append("## Top queries (por impresiones)")
        for q in queries[:15]:
            summary.append(
                f"- \"{q['keys'][0]}\" — {q['clicks']} clicks, "
                f"{q['impressions']} imp, CTR {q['ctr']}%, pos {q['position']}"
            )
        summary.append("")

    # Top pages
    pages = data.get("top_pages", [])
    if pages:
        summary.append("## Top pages (por clicks)")
        for p in pages[:15]:
            slug = p["keys"][0].split("/")[-2] if p["keys"][0].endswith("/") else p["keys"][0].split("/")[-1]
            summary.append(
                f"- {slug} — {p['clicks']} clicks, "
                f"{p['impressions']} imp, CTR {p['ctr']}%, pos {p['position']}"
            )
        summary.append("")

    # Oportunidades (alto imp, bajo CTR, posicion < 20)
    opportunities = [
        q for q in queries
        if q["impressions"] >= 10 and q["ctr"] < 3.0 and q["position"] < 20
    ]
    if opportunities:
        summary.append("## Oportunidades (alto imp, bajo CTR, pos < 20)")
        for q in opportunities[:10]:
            summary.append(
                f"- \"{q['keys'][0]}\" — pos {q['position']}, "
                f"{q['impressions']} imp, CTR {q['ctr']}%"
            )
        summary.append("")

    return "\n".join(summary)


def main():
    parser = argparse.ArgumentParser(description="Fetch Google Search Console data")
    parser.add_argument("--days", type=int, default=7, help="Dias de datos (default 7)")
    parser.add_argument("--auth", action="store_true", help="Solo autenticar")
    parser.add_argument("--summary", action="store_true", help="Imprimir resumen en consola")
    parser.add_argument("--site", type=str, default=None, help="Site URL (ej: sc-domain:iacedemy.com, sc-domain:riskitera.com)")
    parser.add_argument("--all", action="store_true", help="Fetch todos los sites disponibles")
    parser.add_argument("--list", action="store_true", help="Listar sites disponibles y salir")
    args = parser.parse_args()

    ensure_dirs()
    creds = get_credentials()

    if args.auth:
        print("[OK] Autenticacion completada.")
        return

    service = get_service(creds)

    if args.list:
        result = service.sites().list().execute()
        sites = result.get("siteEntry", [])
        print("Sites disponibles:")
        for s in sites:
            print(f"  {s['siteUrl']:40s}  {s.get('permissionLevel', '')}")
        return

    if args.all:
        result = service.sites().list().execute()
        sites = result.get("siteEntry", [])
        for s in sites:
            url = s["siteUrl"]
            print(f"\n{'='*60}")
            print(f"  {url}")
            print(f"{'='*60}")
            _fetch_site(service, url, args)
        return

    if args.site:
        site_url = args.site
        print(f"[OK] Usando site: {site_url}")
    else:
        site_url = detect_site_url(service)

    _fetch_site(service, site_url, args)


def _fetch_site(service, site_url, args):
    """Fetch data for a single site."""
    # Site slug for file naming (sc-domain:iacedemy.com → iacedemy.com)
    site_slug = site_url.replace("sc-domain:", "").replace("https://", "").replace("/", "").replace(":", "_")
    site_dir = DATA_DIR / site_slug
    site_dir.mkdir(parents=True, exist_ok=True)

    # GSC data has ~3 day delay
    end_date = (datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=3 + args.days)).strftime("%Y-%m-%d")

    print(f"[INFO] Fetching {start_date} a {end_date} para {site_url}")

    try:
        queries_raw = fetch_queries(service, site_url, start_date, end_date)
        pages_raw = fetch_pages(service, site_url, start_date, end_date)
        daily_raw = fetch_daily_totals(service, site_url, start_date, end_date)
        by_page_raw = fetch_queries_by_page(service, site_url, start_date, end_date)
    except Exception as e:
        print(f"[ERROR] {site_url}: {e}")
        return

    data = {
        "fetched_at": datetime.now().isoformat(),
        "site_url": site_url,
        "period": {"start": start_date, "end": end_date, "days": args.days},
        "top_queries": [format_row(r) for r in queries_raw.get("rows", [])],
        "top_pages": [format_row(r) for r in pages_raw.get("rows", [])],
        "daily_totals": {
            "rows": [format_row(r) for r in daily_raw.get("rows", [])]
        },
        "queries_by_page": [format_row(r) for r in by_page_raw.get("rows", [])],
    }

    # Save to site-specific directory
    today = datetime.now().strftime("%Y-%m-%d")
    json_path = site_dir / f"{today}.json"
    json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    print(f"[OK] Datos guardados en {json_path}")

    summary = generate_summary(data)
    summary_path = site_dir / f"{today}.md"
    summary_path.write_text(summary)
    print(f"[OK] Resumen guardado en {summary_path}")

    # Latest symlinks
    latest_json = site_dir / "latest.json"
    latest_json.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    latest_md = site_dir / "latest.md"
    latest_md.write_text(summary)

    # Also save to root DATA_DIR for backwards compat (default site only)
    if not hasattr(args, '_multi') or not args._multi:
        root_json = DATA_DIR / f"{today}.json"
        root_json.write_text(json.dumps(data, indent=2, ensure_ascii=False))
        root_latest = DATA_DIR / "latest.json"
        root_latest.write_text(json.dumps(data, indent=2, ensure_ascii=False))
        root_md = DATA_DIR / f"{today}.md"
        root_md.write_text(summary)
        root_latest_md = DATA_DIR / "latest.md"
        root_latest_md.write_text(summary)

    if args.summary:
        print()
        print(summary)

    print(f"[DONE] {site_slug}: {len(data['top_queries'])} queries, {len(data['top_pages'])} pages")


if __name__ == "__main__":
    main()
