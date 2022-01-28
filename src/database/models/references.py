from uuid import uuid4
from tortoise.fields.data import TextField

from tortoise.models import Model
from tortoise.fields import IntField, CharField, UUIDField


class RequirementActType(Model):
    id = IntField(pk=True)
    uid = UUIDField(default=uuid4)
    title = CharField(max_length=255, unique=True)
    regex = CharField(max_length=255)

    class Meta:
        app = "references"
        table = "ref_acts"
        table_description = "Типы актов"
        ordering=["id"]


    class PydanticMeta:
        exclude = []
        include = []


class RequirementSubject(Model):
    id = IntField(pk=True)
    uid = UUIDField(default=uuid4)
    title = CharField(max_length=255, unique=True)
    regex = CharField(max_length=255)

    class Meta:
        app = "references"
        table = "ref_subjects"
        table_description = "Типы субъектов"
        ordering=["id"]


    class PydanticMeta:
        exclude = []
        include = []


class RequirementPublicationStatus(Model):
    id = IntField(pk=True)
    uid = UUIDField(default=uuid4)
    title = CharField(max_length=255, unique=True)
    regex = CharField(max_length=255)

    class Meta:
        app = "references"
        table = "ref_publication_status"
        table_description = "Статусы субъектов"
        ordering=["id"]


    class PydanticMeta:
        exclude = []
        include = []


class RequirementWorkStatus(Model):
    id = IntField(pk=True)
    uid = UUIDField(default=uuid4)
    title = CharField(max_length=255, unique=True)
    regex = CharField(max_length=255)
    table_description = "С"

    class Meta:
        app = "references"
        table = "ref_work_status"
        ordering=["id"]


    class PydanticMeta:
        exclude = []
        inclde = []


class RequirementValidityStatus(Model):
    id = IntField(pk=True)
    uid = UUIDField(default=uuid4)
    title = CharField(max_length=255, unqiue=True)
    regex = CharField(max_length=255)

    class Meta:
        app = "references"
        table = "ref_validity_status"
        ordering=["id"]


    class PydanticMeta:
        exclude = []
        inclde = []


__models__ = [
    RequirementActType,
    RequirementPublicationStatus,
    RequirementSubject,
    RequirementValidityStatus,
    RequirementWorkStatus
]
