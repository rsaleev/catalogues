from typing import Union

from uuid import UUID

from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import status, BackgroundTasks

from tortoise.exceptions import IntegrityError, FieldError

import re

from src.service.schemas.references import (
    RequirementActType,
    RequirementActTypeView,
    RequirementActTypesView,
    RequirementActTypeData,
)
from src.database.helpers import recalc_pk

router = APIRouter(prefix="/references/requirement/act",tags=["Тип акта ОТ"])

@router.get(
    "/types",
    response_model=RequirementActTypesView,
    description="Список типов актов ОТ",
)
async def get_types():
    records = await RequirementActTypesView.from_queryset(RequirementActType.all())
    return records

@router.get(
    "/types/id/{id}",
    response_model=RequirementActTypeView,
    description="Тип акта ОТ по ID записи",
)
async def get_act_by_id(id: int):
    record = await RequirementActTypeView.from_queryset_single(
        RequirementActType.get_or_none(id=id)
    )
    if record:
        return record
    else:
        raise HTTPException(status_code=404, detail="Запись не найдена")


@router.get(
    "/types/guid/{guid}",
    response_model=RequirementActTypeView,
    description="Статус публикации ОТ по GUID записи",
)
async def get_status_by_guid(guid: UUID):
    record = await RequirementActTypeView.from_queryset_single(
        RequirementActType.get_or_none(guid=guid)
    )
    if record:
        return record
    else:
        raise HTTPException(status_code=404, detail="Запись не найдена")

@router.get(
    "/types/title/{title}",
    response_model=RequirementActTypeView,
    description="Поиск статуса публикации ОТ по описанию",
    status_code=status.HTTP_200_OK
)
async def get_act_by_title(title: str):
    """
    Поиск осуществляется по регулярному выражению, записанному в таблице в атрибуте regex
    """
    records = await RequirementActType.all()
    result: Union[RequirementActType, None] = next(
        (r for r in records if re.match(r.regex, title, flags=re.I)), None
    )
    if result:
        record = RequirementActTypeView.from_orm(result)
        return record
    else:
        raise HTTPException(status_code=404, detail="Запись не найдена")


@router.put("/types/id/{id}", status_code=status.HTTP_200_OK, description="Изменение записи по ID")
async def update_act_by_id(id: int, data: RequirementActTypeData):
    record = await RequirementActType.get_or_none(id=id)
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


@router.put("/types/guid/{guid}", status_code=status.HTTP_200_OK, description="Изменение записи по GUID")
async def update_act_by_guid(guid: UUID, data: RequirementActTypeData):
    record = await RequirementActType.get_or_none(uid=guid)
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

@router.post("/types", status_code=status.HTTP_201_CREATED, description="Создание типа акта")
async def create_act(data:RequirementActTypeData):
    if not data.title or not data.regex:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Тело запроса не соответствует схеме",
        )
    record = await RequirementActType.get_or_none(title=data.title)
    if not record:
        try:
            await RequirementActType.create(**data.dict())
        except (FieldError, IntegrityError):
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Ошибка создания записи",
            )
        else:
            return 
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Запись уже существует"
        )

@router.delete(
    "/types/guid/{guid}",
    status_code=status.HTTP_202_ACCEPTED,
    description="Удаление записи статуса публикации по GUID",
)
async def delete_type_by_guid(guid: UUID, background_tasks: BackgroundTasks):
    record = await RequirementActType.get_or_none(uid=guid)
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
        background_tasks.add_task(recalc_pk, RequirementActType)
        return status.HTTP_200_OK
        

@router.delete(
    "/types/id/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    description="Удаление записи статуса публикации по GUID",
)
async def delete_status_by_id(id: int, background_tasks: BackgroundTasks):
    record = await RequirementActType.get_or_none(id=id)
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
        background_tasks.add_task(recalc_pk, RequirementActType)
        return status.HTTP_200_OK

  