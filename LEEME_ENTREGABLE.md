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
