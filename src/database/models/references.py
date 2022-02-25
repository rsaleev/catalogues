from uuid import uuid4

from tortoise.models import Model
from tortoise.fields import IntField, CharField, UUIDField, TextField


__title__ = "Справочная информация по атрибутам ОТ"

class ReferenceBaseModel(Model):
    id = IntField(pk=True, description="Первичный ключ")
    uid = UUIDField(default=uuid4, description="Уникальный идентификатор")
    title = CharField(max_length=255, unique=True, description="Описание")
    regex = CharField(
        max_length=255, description="Описание в виде паттерна регулярного выражения"
    )
    code = IntField(null=False, description="Значение в виде кода (целое число)")

    class Meta:
        abstract=True


class RequirementActType(ReferenceBaseModel):
    class Meta:
        app = "references"
        table = "ref_acts"
        table_description = "Типы актов"
        ordering = ["id"]

    class PydanticMeta:
        exclude = ["id"]
        include = []


class RequirementSubject(ReferenceBaseModel):
    class Meta:
        app = "references"
        table = "ref_subjects"
        table_description = "Типы субъектов"
        ordering = ["id"]

    class PydanticMeta:
        exclude = ["id"]
        include = []


class RequirementPublicationStatus(ReferenceBaseModel):
    class Meta:
        app = "references"
        table = "ref_publication_status"
        table_description = "Статусы публикации"
        ordering = ["id"]

    class PydanticMeta:
        exclude = ["id"]
        include = []


class RequirementWorkStatus(ReferenceBaseModel):
    class Meta:
        app = "references"
        table = "ref_work_status"
        ordering = ["id"]
        table_description = "Статусы работы с ОТ"


    class PydanticMeta:
        exclude = ["id"]
        inclde = []


class RequirementValidityStatus(ReferenceBaseModel):
    class Meta:
        app = "references"
        table = "ref_validity_status"
        ordering = ["id"]
        table_description = "Статусы действия ОТ"


    class PydanticMeta:
        exclude = ["id"]
        inclde = []


class RequirementControlOrganization(ReferenceBaseModel):

    #gisok_alias = TextField()
    class Meta:
        app = "references"
        table = "ref_control_org"
        ordering = ["id"]
        table_description = "Органы, проверяющие на соответствие ОТ; органы, выдающие информацию и т.д."


    class PydanticMeta:
        exclude = ["id"]
        inclde = []

class RequirementControlLevel(ReferenceBaseModel):

     class Meta:
        app = "references"
        table = "ref_control_level"
        ordering = ["id"]
        table_description = "Уровень контроля ОТ"


class RequirementRegulationLevel(ReferenceBaseModel):

     class Meta:
        app = "references"
        table = "ref_regulation_level"
        ordering = ["id"]
        table_description = "Уровень регулирования ОТ"

class RequirementEvaluationForm(ReferenceBaseModel):

    class Meta:
        app = "references"
        table = "ref_evaluation_form"
        ordering = ["id"]
        table_description = "Форма оценки соблюдения ОТ"



__models__ = [
    RequirementActType,
    RequirementPublicationStatus,
    RequirementSubject,
    RequirementValidityStatus,
    RequirementWorkStatus,
    RequirementControlOrganization,
    RequirementControlLevel,
    RequirementRegulationLevel,
    RequirementEvaluationForm
]
