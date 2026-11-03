<<<<<<< HEAD
"""Endpoints de recomendaciones generadas por IA (origen 'ia') y su revisión humana."""

from typing import Literal

from fastapi import APIRouter, status

from api.schemas import RecomendacionSalida, RevisionEntrada
from core import database, ia_service
=======
"""Endpoints de recomendaciones generadas por IA (origen 'ia') y su revisión humana.

La generación (POST /recomendaciones/{resultado_id}) se agrega en la Fase 4.
"""

from typing import Literal

from fastapi import APIRouter

from api.schemas import RecomendacionSalida, RevisionEntrada
from core import database
>>>>>>> 9559d6114f31926bd85adc58ce52afe2ca020610

router = APIRouter(prefix="/recomendaciones", tags=["Recomendaciones (IA)"])


<<<<<<< HEAD
@router.post("/{resultado_id}", response_model=RecomendacionSalida,
             status_code=status.HTTP_201_CREATED,
             summary="Generar con IA una recomendación para un resultado de matching",
             responses={404: {"description": "El resultado no existe"},
                        409: {"description": "El resultado no tiene competencias faltantes"},
                        502: {"description": "La IA respondió algo inválido (2 intentos)"},
                        503: {"description": "Servicio de IA no disponible"}})
def generar_recomendacion(resultado_id: int):
    """Usa las competencias faltantes **ya calculadas por reglas** para pedirle a la IA
    recomendaciones de formación. Se guarda con estado `pendiente_revision`."""
    return ia_service.generar_y_guardar(resultado_id)


=======
>>>>>>> 9559d6114f31926bd85adc58ce52afe2ca020610
@router.get("", response_model=list[RecomendacionSalida], summary="Listar recomendaciones de IA")
def listar_recomendaciones(
    estado: Literal["pendiente_revision", "aprobada", "rechazada"] | None = None,
):
    return database.listar_recomendaciones(estado=estado)


@router.get("/{recomendacion_id}", response_model=RecomendacionSalida,
            summary="Detalle de una recomendación", responses={404: {"description": "No existe"}})
def obtener_recomendacion(recomendacion_id: int):
    return database.obtener_recomendacion(recomendacion_id)


@router.patch("/{recomendacion_id}/revision", response_model=RecomendacionSalida,
              summary="Supervisión humana: aprobar o rechazar una recomendación",
              responses={404: {"description": "No existe"},
                         409: {"description": "Ya fue revisada"},
                         422: {"description": "Estado inválido"}})
def revisar_recomendacion(recomendacion_id: int, datos: RevisionEntrada):
    return database.revisar_recomendacion(recomendacion_id, datos.estado, datos.comentario)
