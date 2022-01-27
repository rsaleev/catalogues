from typing import Union
from uuid import UUID

from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import status, Response

from tortoise.exceptions import FieldError, IntegrityError

import re

from src.service.models.references import (
    RequirementPublicationStatus,
    RequirementPublicationStatusView,
    RequirementPublicationStatusesView,
    RequirementPublicationStatusData,
)

router = APIRouter(prefix="/references/requirement/publication")


@router.get(
    "/statuses",
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
    "/statuses/id/{id}",
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
    "/statuses/guid/{guid}",
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
    "/statuses/title/{title}",
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
    "/statuses/id/{id}",
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
    "/statuses/guid/{guid}",
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
        return status.HTTP_202_ACCEPTED
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ошибка обновления записи",
        )
       


@router.delete(
    "/statuses/guid/{guid}",
    status_code=status.HTTP_202_ACCEPTED,
    description="Удаление записи статуса публикации по GUID",
)
async def delete_status_by_guid(guid: UUID):
    try:
        record = await RequirementPublicationStatus.get_or_none(uid=guid)
        if record:
            try:
                await record.delete()
                return status.HTTP_200_OK
            except:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Ошибка удаления записи",
                )

        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Запись уже существует",
            )
    except (FieldError, IntegrityError):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка создания записи",
        )


@router.delete(
    "/statuses/id/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    description="Удаление записи статуса публикации по GUID",
)
async def delete_status_by_id(id: int):
    try:
        record = await RequirementPublicationStatus.get_or_none(id=id)
        if record:
            try:
                await record.delete()
                return
            except:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Ошибка удаления записи",
                )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Запись уже существует",
            )
    except (FieldError, IntegrityError):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка создания записи",
        )


@router.post(
    "/statuses",
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
  
