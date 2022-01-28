from typing import Union, Type
from uuid import UUID

from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import status, Response, BackgroundTasks

from tortoise.exceptions import FieldError, IntegrityError

import re

from src.service.models.references import (
    RequirementSubject,
    RequirementSubjectTypeData,
    RequirementSubjectTypeView,
    RequirementSubjectTypesView
)
from src.database.helpers import recalc_pk


router = APIRouter(prefix="/references/requirement/subjects", tags=['Типы субъектов'])


@router.get(
    "/types",
    response_model=RequirementSubjectTypesView,
    description="Список типо субъектов ОТ",
    status_code=status.HTTP_200_OK,
)
async def get_types():
    records = await RequirementSubjectTypesView.from_queryset(
        RequirementSubject.all()
    )
    return records


@router.get(
    "/types/id/{id}",
    response_model=RequirementSubjectTypeView,
    description="Тип субъекта ОТ по ID записи",
    status_code=status.HTTP_200_OK,
)
async def get_status_by_id(id: int):
    record = await RequirementSubjectTypeView.from_queryset_single(
        RequirementSubject.get_or_none(id=id)
    )
    if record:
        return record
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Запись не найдена"
        )


@router.get(
    "/types/guid/{guid}",
    response_model=RequirementSubjectTypeView,
    description="Тип субъекта ОТ по GUID записи",
)
async def get_status_by_guid(guid: UUID):
    record = await RequirementSubjectTypeView.from_queryset_single(
        RequirementSubject.get_or_none(uid=guid)
    )
    if record:
        return record
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Запись не найдена"
        )


@router.get(
    "/types/title/{title}",
    response_model=RequirementSubjectTypeView,
    description="Поиск типа субъекта ОТ по описанию",
)
async def get_status_by_title(title: str):
    """
    Поиск осуществляется по регулярному выражению, записанному в таблице в атрибуте regex
    """
    records = await RequirementSubject.all()
    result: Union[RequirementSubject, None] = next(
        (r for r in records if re.match(r.regex, title, flags=re.I)), None
    )
    if result:
        record = RequirementSubjectTypeView.from_orm(result)
        return record
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Запись не найдена"
        )


@router.put(
    "/types/id/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    description="Обновление записи типа субъекта по ID",
)
async def update_status_by_id(id: int, data: RequirementSubjectTypeData):
    record = await RequirementSubject.get_or_none(id=id)
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
    "/types/guid/{guid}",
    status_code=status.HTTP_202_ACCEPTED,
    description="Обновление записи типа субъекта по GUID",
)
async def update_status_by_guid(guid: UUID, data: RequirementSubjectTypeData):
    record = await RequirementSubject.get_or_none(uid=guid)
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
    "/types/guid/{guid}",
    status_code=status.HTTP_202_ACCEPTED,
    description="Удаление записи типа субъекта по GUID",
)
async def delete_status_by_guid(guid: UUID,background_tasks: BackgroundTasks):
    record = await RequirementSubject.get_or_none(uid=guid)
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
        background_tasks.add_task(recalc_pk, RequirementSubject)
        return status.HTTP_200_OK
        

@router.delete(
    "/types/id/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    description="Удаление записи типа субъекта по ID",
)
async def delete_status_by_id(id: int, background_tasks: BackgroundTasks):
    record = await RequirementSubject.get_or_none(id=id)
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
        background_tasks.add_task(recalc_pk, RequirementSubject)
        return status.HTTP_200_OK


@router.post(
    "/types",
    status_code=status.HTTP_201_CREATED,
    description="Создание нового типа субъекта ОТ",
)
async def create_new_status(data: RequirementSubjectTypeData):
    if not data.title or not data.regex:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Тело запроса не соответствует схеме",
        )
    record = await RequirementSubject.get_or_none(title=data.title)
    if not record:
        try:
            await RequirementSubject.create(**data.dict())
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
  
