from typing import List

from itertools import groupby

from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import status

from tortoise.models import Model as ORMModel

from src.database.models import references
from src.database.models import ervk
from src.database.models import okved

from src.service.schemas.catalogues import CatalogueName, Catalogues, ORMModelDescription


router = APIRouter(prefix="/catalogues", tags=['Список справочников в системе'])


def fetch_catalogues()->List[CatalogueName]:
    """
    fetch_catalogues 

    Загрузка каталогов в единый массив с преобразованием в объекты Pydantic

    Returns:
        List[CatalogueName]: массив каталогов
    """
    all_models = []
    references_models: List[ORMModel] = references.__models__
    ervk_models: List[ORMModel] = ervk.__models__
    okved_models: List[ORMModel] = okved.__models__
    organizations: List[ORMModel] = []
    all_models.extend(references_models)
    all_models.extend(ervk_models)
    all_models.extend(okved_models)
    all_models.extend(organizations)
    all_models = [ORMModelDescription(**m.describe()) for m in all_models]
    catalogues_list = [ct for ct in all_models if not ct.abstract]
    catalogues_grouped = [
        CatalogueName(**{"title": k, "data": [desc.dict() for desc in g]})
        for k, g in groupby(catalogues_list, key=lambda o: o.app)
    ]
    return catalogues_grouped


@router.get(
    "/",
    response_model=Catalogues,
    description="Получение списка справочников",
    status_code=status.HTTP_200_OK,
)
async def get_all_catalogues():
    try:
        response = Catalogues(catalogues=fetch_catalogues())
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Записи отсутствуют")
    return response


@router.get(
    "/title/{title}",
    response_model=CatalogueName,
    description="Получение справочника по наименованию",
    status_code=status.HTTP_200_OK,
)
async def get_catalogue_by_name(title):
    response = next((cat for cat in fetch_catalogues() if cat.title == title), None)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Запись отсутствует")
    return response
