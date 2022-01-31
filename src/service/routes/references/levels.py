from typing import Union

from uuid import UUID

from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import status

from tortoise.exceptions import IntegrityError, FieldError

import re

from src.service.schemas.references import (
    RequirementControlLevel,
    RequirementControlLevelData,
    RequirementControlLevelView,
    RequirementControlLevelsView

)

router = APIRouter(prefix="/references/levels",tags=["Виды контроля ОТ"])

@router.get(
    "",
    response_model=RequirementControlLevelView,
    description="Список видов контроля",
)
async def get_acts():
    records = await RequirementControlLevelView.from_queryset(RequirementControlLevel.all())
    return records

@router.get(
    "/id/{id}",
    response_model=RequirementControlLevelView,
    description="Тип акта ОТ по ID записи",
)
async def get_act_by_id(id: int):
    record = await RequirementControlLevelView.from_queryset_single(
        RequirementControlLevel.get_or_none(id=id)
    )
    if record:
        return record
    else:
        raise HTTPException(status_code=404, detail="Запись не найдена")

router.get(
    "/guid/{guid}",
    response_model=RequirementControlLevelView,
    description="Статус публикации ОТ по GUID записи",
)
async def get_status_by_guid(guid: UUID):
    record = await RequirementControlLevelView.from_queryset_single(
        RequirementControlLevel.get_or_none(guid=guid)
    )
    if record:
        return record
    else:
        raise HTTPException(status_code=404, detail="Запись не найдена")

@router.get(
    "/acts/title/{title}" ,response_model=RequirementControlLevelView,
    description="Поиск статуса публикации ОТ по описанию",
    status_code=status.HTTP_200_OK
)
async def get_act_by_title(title: str):
    """
    Поиск осуществляется по регулярному выражению, записанному в таблице в атрибуте regex
    """
    records = await RequirementControlLevel.all()
    result: Union[RequirementControlLevel, None] = next(
        (r for r in records if re.match(r.regex, title, flags=re.I)), None
    )
    if result:
        record = RequirementControlLevelView.from_orm(result)
        return record
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Запись не найдена")


@router.put("/acts/id/{id}", status_code=status.HTTP_200_OK, description="Изменение записи по ID")
async def update_act_by_id(id: int, data: RequirementControlLevelData):
    record = await RequirementControlLevel.get_or_none(id=id)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Запись не найдена"
        )
    try:
        await record.update_from_dict(data.dict(exclude_unset=True))
        return
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ошибка обновления записи",
        )


@router.put("/acts/guid/{guid}", status_code=status.HTTP_200_OK, description="Изменение записи по GUID")
async def update_act_by_guid(guid: UUID, data: RequirementControlLevelData):
    record = await RequirementControlLevel.get_or_none(uid=guid)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Запись не найдена"
        )
    try:
        await record.update_from_dict(data.dict(exclude_unset=True))
        return 
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ошибка обновления записи",
        )

@router.post("/acts", status_code=status.HTTP_201_CREATED, description="Создание типа акта")
async def create_act(data:RequirementControlLevelData):
    if not data.title or not data.regex:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Тело запроса не соответствует схеме",
        )
    record = await RequirementControlLevel.get_or_none(title=data.title)
    if not record:
        try:
            await RequirementControlLevel.create(**data.dict())
        except (FieldError, IntegrityError):
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Ошибка создания за",
            )
        else:
            return 
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Запись уже существует"
        )

@router.delete(
    "/acts/guid/{guid}",
    status_code=status.HTTP_202_ACCEPTED,
    description="Удаление записи статуса публикации по GUID",
)
async def delete_type_by_guid(guid: UUID):
    record = await RequirementControlLevel.get_or_none(uid=guid)
    if not record:
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Ошибка удаления записи",
            )
    try:
        await record.delete()
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Запись не существует",
        )
    else:
        return status.HTTP_200_OK
        

@router.delete(
    "/acts/id/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    description="Удаление записи статуса публикации по GUID",
)
async def delete_status_by_id(id:int):
    record = await RequirementControlLevel.get_or_none(id=id)
    if not record:
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Ошибка удаления записи",
            )
    try:
        await record.delete()
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Запись не существует",
        )
    else:
        return status.HTTP_200_OK

  