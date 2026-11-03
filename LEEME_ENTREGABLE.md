<<<<<<< HEAD
# Entregable 3 de 4 — Inteligencia artificial local (Ollama)

Se suma al Entregable 2 la generación de recomendaciones con IA y la revisión humana.

## Qué se agrega
- `core/ia_service.py`: cliente de Ollama (`llama3.2:3b`), prompt en español con las faltantes ya
  calculadas por reglas, validación de la respuesta con Pydantic y 1 reintento.
- `POST /recomendaciones/{resultado_id}`: 404, 502 (respuesta inválida) y 503 (IA caída).
- Toda recomendación queda `pendiente_revision`; solo un humano la aprueba o rechaza.
- `tests/test_ia.py`: 12 tests nuevos con Ollama mockeado (53 en total).

## Requisito extra
Ollama instalado y el modelo descargado: `ollama pull llama3.2:3b`.

## Cómo probarlo
```powershell
pip install -r requirements.txt
pytest -v                          # 53 tests, no necesitan Ollama
python scripts/seed.py --reset
uvicorn api.main:app --reload
streamlit run ui/app.py
```
En la interfaz: Matching → calcular → Recomendaciones IA → Generar → Aprobar/Rechazar con comentario.
Error a mostrar: cerrar Ollama y generar → "Servicio de IA no disponible" (503), el resto sigue andando.
=======
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
>>>>>>> 9559d6114f31926bd85adc58ce52afe2ca020610
