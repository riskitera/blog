.DEFAULT_GOAL := help
.PHONY: help install dev build new-post new-case clean deploy lint serve

# ──────────────────────────────────────────────
# Riskitera Blog - Hugo + Tailwind CSS
# ──────────────────────────────────────────────

help: ## Show available commands
	@echo ""
	@echo "  Riskitera Blog - Available commands:"
	@echo "  ─────────────────────────────────────"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo ""

install: ## Install dependencies (npm packages for Tailwind CSS)
	npm install

dev: ## Start development server with live reload and drafts
	@echo "Starting Tailwind CSS watcher + Hugo server..."
	@npm run build:css
	hugo server --buildDrafts --disableFastRender --navigateToChanged

serve: ## Start production-like server (no drafts)
	@npm run build:css
	hugo server --disableFastRender

build: ## Build production site (minified, purged CSS)
	npm run build:css
	hugo --minify --gc
	@echo ""
	@echo "✓ Site built in public/"
	@echo "  Files: $$(find public -name '*.html' | wc -l | tr -d ' ') HTML pages"

new-post: ## Create a new blog post (usage: make new-post SLUG=my-post LANG=es)
	@if [ -z "$(SLUG)" ]; then \
		echo "Usage: make new-post SLUG=my-post-slug [LANG=es]"; \
		echo "  SLUG: URL-friendly name for the post (required)"; \
		echo "  LANG: Language code, default 'es' (optional)"; \
		exit 1; \
	fi
	hugo new content/$(or $(LANG),es)/posts/$(SLUG)/index.md
	@echo ""
	@echo "✓ Post created: content/$(or $(LANG),es)/posts/$(SLUG)/index.md"
	@echo "  Edit the file and set draft: false when ready to publish"

new-case: ## Create a new case study (usage: make new-case SLUG=company-name LANG=es)
	@if [ -z "$(SLUG)" ]; then \
		echo "Usage: make new-case SLUG=company-name [LANG=es]"; \
		echo "  SLUG: URL-friendly name for the case study (required)"; \
		echo "  LANG: Language code, default 'es' (optional)"; \
		exit 1; \
	fi
	hugo new content/$(or $(LANG),es)/case-studies/$(SLUG)/index.md
	@echo ""
	@echo "✓ Case study created: content/$(or $(LANG),es)/case-studies/$(SLUG)/index.md"
	@echo "  Edit the file and set draft: false when ready to publish"

clean: ## Clean generated files (public/, resources/, CSS output)
	rm -rf public/ resources/_gen/
	@echo "✓ Cleaned public/ and resources/_gen/"

deploy: build ## Build and show Cloudflare Pages deploy instructions
	@echo ""
	@echo "  Cloudflare Pages Configuration:"
	@echo "  ─────────────────────────────────"
	@echo "  Build command:  hugo --minify"
	@echo "  Build output:   public/"
	@echo "  Env variable:   HUGO_VERSION = 0.152.2"
	@echo "  Custom domain:  blog.riskitera.com"
	@echo ""
	@echo "  For CI/CD, push to the configured branch."

lint: build ## Build and validate generated HTML
	@echo ""
	@echo "  Build Validation:"
	@echo "  ─────────────────"
	@echo "  HTML files:  $$(find public -name '*.html' | wc -l | tr -d ' ')"
	@echo "  XML files:   $$(find public -name '*.xml' | wc -l | tr -d ' ')"
	@echo "  JSON files:  $$(find public -name '*.json' | wc -l | tr -d ' ')"
	@echo ""
	@echo "  Checking for broken internal links..."
	@broken=0; \
	for f in $$(find public -name '*.html'); do \
		hrefs=$$(grep -oP 'href="(/[^"]*)"' "$$f" 2>/dev/null | grep -oP '"/[^"]*"' | tr -d '"'); \
		for href in $$hrefs; do \
			target="public$${href}"; \
			if [ ! -f "$$target" ] && [ ! -f "$${target}index.html" ] && [ ! -d "$$target" ]; then \
				echo "  ⚠ Broken: $$href (in $$f)"; \
				broken=$$((broken + 1)); \
			fi; \
		done; \
	done; \
	if [ "$$broken" -eq 0 ]; then echo "  ✓ No broken internal links found"; fi
