from nis import cat
from typing import ChainMap, List

from itertools import groupby

from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import status

from tortoise.models import Model as ORMModel

from src.database.models.catalogues import references
from src.database.models.catalogues import ervk
from src.database.models.catalogues import okved
from src.database.models.catalogues import organizations

from src.service.models.catalogues import Catalogues, ORMModelDescription, CatalogueName


router = APIRouter(prefix="/catalogues")


def fetch_catalogues():
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
    description="Получить список справочников",
    status_code=status.HTTP_200_OK,
)
async def get_all_catalogues():
    response = Catalogues(catalogues=fetch_catalogues())
    return response


@router.get(
    "/title/{title}",
    response_model=CatalogueName,
    description="Получить справочник по наименованию",
    status_code=status.HTTP_200_OK,
)
async def get_catalogue_by_name(title):
    response = next((cat for cat in fetch_catalogues() if cat.title == title), None)
    if response:
        return response
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
