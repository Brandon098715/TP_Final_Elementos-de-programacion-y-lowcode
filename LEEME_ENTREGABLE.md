<<<<<<< HEAD
# Entregable 2 de 4 — Interfaz Streamlit sobre el backend

Se suma al Entregable 1 la interfaz de usuario. Streamlit consume **solo la API**, nunca la base.

## Qué se agrega
- `ui/app.py` y `ui/paginas/`: Estudiantes (alta, filtros, edición), Ofertas, Matching (ranking con
  colores, desglose y faltantes, etiqueta "Calculado por reglas"), Recomendaciones y Reportes.
- `ui/api_client.py`: todas las llamadas HTTP, con mensajes comprensibles ante errores de conexión.
- Indicador del estado de `/health` en la barra lateral.

## Qué NO incluye todavía
La generación real de recomendaciones con IA: la pantalla existe, pero generar da error hasta el
Entregable 3. Tampoco Docker ni n8n.

## Cómo probarlo (dos terminales, con el entorno virtual activado)
```powershell
pip install -r requirements.txt
python scripts/seed.py --reset
uvicorn api.main:app --reload      # terminal 1 → http://localhost:8000/docs
streamlit run ui/app.py            # terminal 2 → http://localhost:8501
```
Probá: crear un estudiante, calcular matching de una oferta, ver Reportes. Para el error de conexión,
cerrá uvicorn y recargá la interfaz. Tests: `pytest -v` (41).
=======
