# Entregable 1 de 4 — Idea y Backend (núcleo Python + API)

**La idea:** plataforma que vincula estudiantes/graduados con ofertas laborales. Calcula un score de
compatibilidad (0–100) con reglas explícitas en Python, identifica competencias faltantes y,
más adelante, usa IA para recomendar formación. Detalle completo en `CONSIGNA_PROYECTO.md`.

## Qué incluye
- `core/`: base SQLite sin ORM, scoring, validaciones, excepciones, matching y reportes.
- `api/`: FastAPI con endpoints de estudiantes, ofertas, matching, recomendaciones (revisión) y reportes.
- `data/seed.json` + `scripts/seed.py`: 8 estudiantes y 5 ofertas ficticias.
- `tests/`: 41 tests (scoring, base de datos, API).

## Qué NO incluye todavía
Interfaz (Entregable 2), generación de recomendaciones con IA (Entregable 3), Docker y n8n (Entregable 4).

## Cómo probarlo
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -v                          # 41 tests
python scripts/seed.py --reset     # carga los datos de ejemplo
uvicorn api.main:app --reload      # API en http://localhost:8000/docs
```
En `/docs` probá: `GET /estudiantes`, `POST /matching/ofertas/1` (ranking con score y faltantes),
`GET /reportes/resumen`, y errores como `GET /estudiantes/999` (404).
