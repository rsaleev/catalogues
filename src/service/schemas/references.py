from typing import Optional

from tortoise.contrib.pydantic.creator import (
    pydantic_model_creator,
    pydantic_queryset_creator,
)

from src.database.models.references import *

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
RequirementWorkStatusesView = pydantic_queryset_creator(RequirementWorkStatus)

# Статус состояния ОТ

class RequirementValidityStatusData(BaseModel):
    """
    Тело запроса для методов POST/PUT
    """

    title: Optional[str] = Field(..., max_length=255, description='Наименование статуса')
    regex: Optional[str] = Field(..., max_length=255, description='Паттерн регулярного выражения')

RequirementValidityStatusView = pydantic_model_creator(RequirementValidityStatus)
RequirementValidityStatusesView = pydantic_queryset_creator(RequirementValidityStatus)

# Уровень контроля
class RequirementControlLevelData(BaseModel):
    """
    Тело запроса для методов POST/PUT
    """
    
    title: Optional[str] = Field(..., max_length=255, description='Наименование уровня контроля')
    regex: Optional[str] = Field(..., max_length=255, description='Паттерн регулярного выражения')

RequirementControlLevelView = pydantic_model_creator(RequirementControlLevel)
RequirementControlLevelsView = pydantic_queryset_creator(RequirementControlLevel)


# Тип организации
class RequirementControlOrgData(BaseModel):
    """
    Тело запроса для методов POST/PUT
    """

    title: Optional[str] = Field(..., max_length=255, description='Наименование уровня контроля')
    regex: Optional[str] = Field(..., max_length=255, description='Паттерн регулярного выражения')

RequirementControlOrgView = pydantic_model_creator(RequirementControlOrganization)
RequirementControlOrgsView = pydantic_queryset_creator(RequirementControlOrganization)


class RequirementRegulationLevelData(BaseModel):
    """
    Тело запроса для методов POST/PUT
    """

    title: Optional[str] = Field(..., max_length=255, description='Наименование уровня регулирования')
    regex: Optional[str] = Field(..., max_length=255, description='Паттерн регулярного выражения')

RequirementRegulationLevelView = pydantic_model_creator(RequirementRegulationLevel)
RequirementRegulationLevelsView = pydantic_queryset_creator(RequirementRegulationLevel)



class RequirementEvaluationFormData(BaseModel):
    """
    Тело запроса для методов POST/PUT
    """

    title: Optional[str] = Field(..., max_length=255, description='Наименование уровня регулирования')
    regex: Optional[str] = Field(..., max_length=255, description='Паттерн регулярного выражения')

RequirementEvaluationFormView = pydantic_model_creator(RequirementEvaluationForm)
RequirementEvaluationFormsView = pydantic_queryset_creator(RequirementEvaluationForm)