from typing import Union
from uuid import UUID

from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import status

from fastapi_cache.decorator import cache


from tortoise.exceptions import FieldError, IntegrityError

import re

from src.service.schemas.references import (
    RequirementValidityStatus,
    RequirementValidityStatusData,
    RequirementValidityStatusView,
    RequirementValidityStatusesView
)


router = APIRouter(prefix="/validity", tags=["Статус ОТ"])


@router.get(
    "/list",
    response_model=RequirementValidityStatusesView,
    description="Список статусов ОТ",
    status_code=status.HTTP_200_OK,
)
async def get_subjects():
    records = await RequirementValidityStatusesView.from_queryset(
       RequirementValidityStatus.all()
    )
    return records


@router.get(
    "/id/{id}",
    response_model=RequirementValidityStatusView,
    description="Тип статуса ОТ по ID записи",
    status_code=status.HTTP_200_OK,
)
async def get_subject_by_id(id: int):
    record = await RequirementValidityStatusView.from_queryset_single(
       RequirementValidityStatus.get_or_none(id=id)
    )
    if record:
        return record
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Запись не найдена"
        )


@router.get(
    "/guid/{guid}",
    response_model=RequirementValidityStatusView,
    description="Тип статуса ОТ по GUID записи",
)
async def get_subject_by_guid(guid: UUID):
    record = await RequirementValidityStatusView.from_queryset_single(
       RequirementValidityStatus.get_or_none(uid=guid)
    )
    if record:
        return record
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Запись не найдена"
        )


@router.get(
    "/title/{title}",
    response_model=RequirementValidityStatusView,
    description="Поиск статуса ОТ по описанию",
)
@cache(expire=60)
async def get_subject_by_title(title: str):
    """
    Поиск осуществляется по регулярному выражению, записанному в таблице в атрибуте regex
    """
    records = await RequirementValidityStatus.all()
    result: Union[RequirementValidityStatus, None] = next(
        (r for r in records if re.match(r.regex, title, flags=re.I)), None
    )
    if result:
        record = RequirementValidityStatusView.from_orm(result)
        return record
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Запись не найдена"
        )


@router.put(
    "/id/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    description="Обновление записи статуса ОТ по ID",
)
async def update_subject_by_id(id: int, data:RequirementValidityStatusData):
    record = await RequirementValidityStatus.get_or_none(id=id)
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
    "/guid/{guid}",
    status_code=status.HTTP_202_ACCEPTED,
    description="Обновление записи статуса ОТ по GUID",
)
async def update_subject_by_guid(guid: UUID, data:RequirementValidityStatusData):
    record = await RequirementValidityStatus.get_or_none(uid=guid)
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
    "/guid/{guid}",
    status_code=status.HTTP_202_ACCEPTED,
    description="Удаление записи статуса ОТ по GUID",
)
async def delete_subject_by_guid(guid: UUID):
    record = await RequirementValidityStatus.get_or_none(uid=guid)
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
    description="Удаление записи статуса ОТ по ID",
)
async def delete_subject_by_id(id: int):
    record = await RequirementValidityStatus.get_or_none(id=id)
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


@router.post(
    " ",
    status_code=status.HTTP_201_CREATED,
    description="Создание нового типа статуса ОТ",
)
async def create_new_subject(data:RequirementValidityStatusData):
    if not data.title or not data.regex:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Тело запроса не соответствует схеме",
        )
    record = await RequirementValidityStatus.get_or_none(title=data.title)
    if not record:
        try:
            await RequirementValidityStatus.create(**data.dict())
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
  
