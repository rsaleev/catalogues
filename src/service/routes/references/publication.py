from typing import Union, Type
from uuid import UUID

from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import status, Response, BackgroundTasks

from tortoise.exceptions import FieldError, IntegrityError

import re

from src.service.schemas.references import (
    RequirementPublicationStatus,
    RequirementPublicationStatusView,
    RequirementPublicationStatusesView,
    RequirementPublicationStatusData,
)
from src.database.helpers import recalc_pk


router = APIRouter(prefix="/references", tags=['Статус публикации ОТ'])


@router.get(
    "/publications",
    response_model=RequirementPublicationStatusesView,
    description="Список статусов публикации ОТ",
    status_code=status.HTTP_200_OK,
)
async def get_statuses():
    records = await RequirementPublicationStatusesView.from_queryset(
        RequirementPublicationStatus.all()
    )
    return records


@router.get(
    "/publications/id/{id}",
    response_model=RequirementPublicationStatusView,
    description="Статус публикации ОТ по ID записи",
    status_code=status.HTTP_200_OK,
)
async def get_status_by_id(id: int):
    record = await RequirementPublicationStatusView.from_queryset_single(
        RequirementPublicationStatus.get_or_none(id=id)
    )
    if record:
        return record
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Запись не найдена"
        )


@router.get(
    "/publications/guid/{guid}",
    response_model=RequirementPublicationStatusView,
    description="Статус публикации ОТ по GUID записи",
)
async def get_status_by_guid(guid: UUID):
    record = await RequirementPublicationStatusView.from_queryset_single(
        RequirementPublicationStatus.get_or_none(uid=guid)
    )
    if record:
        return record
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Запись не найдена"
        )


@router.get(
    "/publications/title/{title}",
    response_model=RequirementPublicationStatusView,
    description="Поиск статуса публикации ОТ по описанию",
)
async def get_status_by_title(title: str):
    """
    Поиск осуществляется по регулярному выражению, записанному в таблице в атрибуте regex
    """
    records = await RequirementPublicationStatus.all()
    result: Union[RequirementPublicationStatus, None] = next(
        (r for r in records if re.match(r.regex, title, flags=re.I)), None
    )
    if result:
        record = RequirementPublicationStatusView.from_orm(result)
        return record
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Запись не найдена"
        )


@router.put(
    "/publications/id/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    description="Обновление записи статуса публикации по ID",
)
async def update_status_by_id(id: int, data: RequirementPublicationStatusData):
    record = await RequirementPublicationStatus.get_or_none(id=id)
    if record:
        try:
            await record.update_from_dict(data.dict(exclude_unset=True))
            return status.HTTP_202_ACCEPTED
        except:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ошибка обновления записи",
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Запись не найдена"
        )


@router.put(
    "/publications/guid/{guid}",
    status_code=status.HTTP_202_ACCEPTED,
    description="Обновление записи статуса публикации по GUID",
)
async def update_status_by_guid(guid: UUID, data: RequirementPublicationStatusData):
    record = await RequirementPublicationStatus.get_or_none(uid=guid)
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
    
@router.delete(
    "/publications/guid/{guid}",
    status_code=status.HTTP_202_ACCEPTED,
    description="Удаление записи статуса публикации по GUID",
)
async def delete_status_by_guid(guid: UUID,background_tasks: BackgroundTasks):
    record = await RequirementPublicationStatus.get_or_none(uid=guid)
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
        background_tasks.add_task(recalc_pk, RequirementPublicationStatus)
        return status.HTTP_200_OK
        

@router.delete(
    "/publications/id/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    description="Удаление записи статуса публикации по ID",
)
async def delete_status_by_id(id: int, background_tasks: BackgroundTasks):
    record = await RequirementPublicationStatus.get_or_none(id=id)
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
        background_tasks.add_task(recalc_pk, RequirementPublicationStatus)
        return status.HTTP_200_OK


@router.post(
    "/publications",
    status_code=status.HTTP_201_CREATED,
    description="Создание нового статуса публикации ОТ",
)
async def create_new_status(data: RequirementPublicationStatusData):
    if not data.title or not data.regex:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Тело запроса не соответствует схеме",
        )
    record = await RequirementPublicationStatus.get_or_none(title=data.title)
    if not record:
        try:
            await RequirementPublicationStatus.create(**data.dict())
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
  