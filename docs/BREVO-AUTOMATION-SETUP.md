# Setup de Automatizacion Brevo — Blog Riskitera Newsletter

## Workflow: Welcome Sequence (5 emails)

### Configuracion en Brevo Dashboard

1. Ir a **Automation > Create a workflow > Custom workflow**
2. Nombre: "Blog Riskitera - Welcome Sequence"

### Trigger
- **Entry point**: Contact added to list
- **List**: "Blog Riskitera Newsletter" (ID=3)

### Secuencia

```
[Trigger: added to list 3]
    |
    v
[Send Email: Template ID=1 "Blog Welcome - Bienvenida"]
    |
    v
[Wait: 2 days]
    |
    v
[Send Email: Template ID=2 "Blog Sequence 2 - Producto"]
    |
    v
[Wait: 3 days]
    |
    v
[Send Email: Template ID=3 "Blog Sequence 3 - Case Study"]
    |
    v
[Wait: 3 days]
    |
    v
[Send Email: Template ID=4 "Blog Sequence 4 - Recurso Gratuito"]
    |
    v
[Wait: 4 days]
    |
    v
[Send Email: Template ID=5 "Blog Sequence 5 - Demo CTA"]
    |
    v
[End]
```

### Resumen de la secuencia

| Dia | Email | Objetivo | Template ID |
|-----|-------|----------|-------------|
| 0 | Bienvenida | Presentacion + 3 articulos recomendados | 1 |
| 2 | Producto | Que es Riskitera (GRC/SOC/CTI) + social proof | 2 |
| 5 | Case Study | Caso real fintech ENS en 6 semanas | 3 |
| 8 | Recurso | Checklist compliance gratuita (lead magnet) | 4 |
| 12 | Demo CTA | Oferta piloto 90 dias + conversion directa | 5 |

### Notas
- Sender: david@riskitera.com (David Moya | Riskitera)
- Reply-to: david@riskitera.com (personal, no noreply)
- Unsubscribe: automatico via {{ unsubscribe }} de Brevo
- Todos los emails tienen dark theme consistente con blog.riskitera.com
