from typing import Optional
from xml.dom import ValidationErr

from tortoise.contrib.pydantic.creator import (
    pydantic_model_creator,
    pydantic_queryset_creator,
)

from src.database.models.catalogues.references import *

from pydantic import BaseModel, Field

"""
https://tortoise-orm.readthedocs.io/en/latest/contrib/pydantic.html
https://tortoise-orm.readthedocs.io/en/latest/examples/pydantic.html#



"""

# Тип акта ОТ


class RequirementActTypeData(BaseModel):
    """

    Тело запроса для методов POST/PUT
    """

    title: Optional[str] = Field(..., max_length=255, description='Наименование статуса')
    regex: Optional[str] = Field(..., max_length=255, description='Паттерн регулярного выражения')


RequirementActTypeView = pydantic_model_creator(RequirementActType)
RequirementActTypesView = pydantic_queryset_creator(RequirementActType)

# Типы субъектов

class RequirementSubjectTypeData(BaseModel):
    """

    Тело запроса для методов POST/PUT
    """

    title: Optional[str] = Field(..., max_length=255, description='Наименование статуса')
    regex: Optional[str] = Field(..., max_length=255, description='Паттерн регулярного выражения')

RequirementSubjectTypeView = pydantic_model_creator(RequirementSubject)
RequirementSubjectTypesView = pydantic_queryset_creator(RequirementSubject)

# Статус публикации ОТ


class RequirementPublicationStatusData(BaseModel):
    """

    Тело запроса для методов POST/PUT
    """

    title: Optional[str] = Field(..., max_length=255, description='Наименование статуса')
    regex: Optional[str] = Field(..., max_length=255, description='Паттерн регулярного выражения')


RequirementPublicationStatusView = pydantic_model_creator(RequirementPublicationStatus)
RequirementPublicationStatusesView = pydantic_queryset_creator(
    RequirementPublicationStatus
)

# Статус работы с ОТ

class RequirementWorkStatusData(BaseModel):
    """

    Тело запроса для методов POST/PUT
    """

    title: Optional[str] = Field(..., max_length=255, description='Наименование статуса')
    regex: Optional[str] = Field(..., max_length=255, description='Паттерн регулярного выражения')

RequirementWorkStatusView = pydantic_model_creator(RequirementWorkStatus)
RequirementWorkStatusViews = pydantic_queryset_creator(RequirementWorkStatus)

# Статус состояния ОТ

class RequirementValidityStatusData(BaseModel):
    """

    Тело запроса для методов POST/PUT
    """

    title: Optional[str] = Field(..., max_length=255, description='Наименование статуса')
    regex: Optional[str] = Field(..., max_length=255, description='Паттерн регулярного выражения')

RequirementValidityStatusView = pydantic_model_creator(RequirementValidityStatus)
RequirementValidityStatusesView = pydantic_queryset_creator(RequirementValidityStatus)

