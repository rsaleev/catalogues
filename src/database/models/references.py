from uuid import uuid4

from tortoise.models import Model
from tortoise.fields import IntField, CharField, UUIDField


__title__ = "Справочная информация по атрибутам ОТ"

class ReferenceBaseModel(Model):
    id = IntField(pk=True, description="Первичный ключ")
    uid = UUIDField(default=uuid4, description="Уникальный идентификатор")
    title = CharField(max_length=255, unique=True, description="Описание")
    regex = CharField(
        max_length=255, description="Описание в виде паттерна регулярного выражения"
    )

    class Meta:
        abstract=True


class RequirementActType(ReferenceBaseModel):
    class Meta:
        app = "references"
        table = "ref_acts"
        table_description = "Типы актов"
        ordering = ["id"]

    class PydanticMeta:
        exclude = []
        include = []


class RequirementSubject(ReferenceBaseModel):
    class Meta:
        app = "references"
        table = "ref_subjects"
        table_description = "Типы субъектов"
        ordering = ["id"]

    class PydanticMeta:
        exclude = []
        include = []


class RequirementPublicationStatus(ReferenceBaseModel):
    class Meta:
        app = "references"
        table = "ref_publication_status"
        table_description = "Статусы публикации"
        ordering = ["id"]

    class PydanticMeta:
        exclude = []
        include = []


class RequirementWorkStatus(ReferenceBaseModel):
    class Meta:
        app = "references"
        table = "ref_work_status"
        ordering = ["id"]
        table_description = "Статусы работы с ОТ"


    class PydanticMeta:
        exclude = []
        inclde = []


class RequirementValidityStatus(ReferenceBaseModel):
    class Meta:
        app = "references"
        table = "ref_validity_status"
        ordering = ["id"]
        table_description = "Статусы действия ОТ"


    class PydanticMeta:
        exclude = []
        inclde = []


class RequirementOrganizationType(ReferenceBaseModel):
    class Meta:
        app = "references"
        table = "ref_organization_type"
        ordering = ["id"]
        table_description = "Органы, проверяющие на соответствие ОТ; органы, выдающие информацию и т.д."


    class PydanticMeta:
        exclude = []
        inclde = []



__models__ = [
    RequirementActType,
    RequirementPublicationStatus,
    RequirementSubject,
    RequirementValidityStatus,
    RequirementWorkStatus,
    RequirementOrganizationType,
]
