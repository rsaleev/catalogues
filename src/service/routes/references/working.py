from typing import Union

from uuid import UUID

from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import status

from fastapi_cache.decorator import cache

from tortoise.exceptions import IntegrityError, FieldError

import re

from src.service.schemas.references import (
    RequirementWorkStatus,
    RequirementWorkStatusView,
    RequirementWorkStatusesView,
    RequirementWorkStatusData,
)

router = APIRouter(prefix="/working", tags=["Статус работы с ОТ"])


@router.get(
    "/list",
    response_model=RequirementWorkStatusesView,
    description="Список статусов работы с ОТ",
)
async def get_working_statuses():
    records = await RequirementWorkStatusesView.from_queryset(
        RequirementWorkStatus.all()
    )
    return records

@router.get(
    "/id/{id}",
    response_model=RequirementWorkStatusView,
    description="Тип акта ОТ по ID записи",
)
async def get_working_status_by_id(id: int):
    record = await RequirementWorkStatusView.from_queryset_single(
        RequirementWorkStatus.get_or_none(id=id)
    )
    if record:
        return record
    else:
        raise HTTPException(status_code=404, detail="Запись не найдена")

@router.get(
    "/guid/{guid}",
    response_model=RequirementWorkStatusView,
    description="Статус работы с ОТ по GUID записи",
)
async def get_working_status_by_guid(guid: UUID):
    record = await RequirementWorkStatusView.from_queryset_single(
        RequirementWorkStatus.get_or_none(guid=guid)
    )
    if record:
        return record
    else:
        raise HTTPException(status_code=404, detail="Запись не найдена")

@router.get(
    "/title/{title}",
    response_model=RequirementWorkStatusView,
    description="Поиск статуса работы с ОТ по описанию",
    status_code=status.HTTP_200_OK,
)
async def get_working_status_by_title(title: str):
    """
    Поиск осуществляется по регулярному выражению, записанному в таблице в атрибуте regex
    """
    records = await RequirementWorkStatus.all()
    result: Union[RequirementWorkStatus, None] = next(
        (r for r in records if re.match(r.regex, title, flags=re.I)), None
    )
    if result:
        record = RequirementWorkStatusView.from_orm(result)
        return record
    else:
        raise HTTPException(status_code=404, detail="Запись не найдена")

@router.put(
    "/id/{id}",
    status_code=status.HTTP_200_OK,
    description="Изменение записи по ID",
)
async def update_working_status_by_id(id: int, data: RequirementWorkStatusData):
    record = await RequirementWorkStatus.get_or_none(id=id)
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

@router.put(
    "/guid/{guid}",
    status_code=status.HTTP_200_OK,
    description="Изменение записи по GUID",
)
async def update_working_status_by_guid(guid: UUID, data: RequirementWorkStatusData):
    record = await RequirementWorkStatus.get_or_none(uid=guid)
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

@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    description="Создание типа статуса работы с ОТ",
)
async def create_working_status(data: RequirementWorkStatusData):
    if not data.title or not data.regex:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Тело запроса не соответствует схеме",
        )
    record = await RequirementWorkStatus.get_or_none(title=data.title)
    if not record:
        try:
            await RequirementWorkStatus.create(**data.dict())
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
    "/guid/{guid}",
    status_code=status.HTTP_202_ACCEPTED,
    description="Удаление записи статуса работы по GUID",
)
async def delete_working_status_by_guid(guid: UUID):
    record = await RequirementWorkStatus.get_or_none(uid=guid)
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
    "/id/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    description="Удаление записи работы по ID",
)
async def delete_working_status_by_id(id: int):
    record = await RequirementWorkStatus.get_or_none(id=id)
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