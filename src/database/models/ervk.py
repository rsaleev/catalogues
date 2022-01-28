from enum import unique
from tortoise.models import Model
from tortoise.fields.data import IntField,UUIDField, CharField
from tortoise.fields.relational import ForeignKeyField, ReverseRelation


__title__ = "Единый реестр видов контроля"
class ControlLevel(Model):
    id = IntField(pk=True)
    uid = UUIDField(index=True, unique=True)
    title = CharField(max_length=255, unique=True)
    code = IntField(index=True)

    types:ReverseRelation["ControlTypes"]
    organizations:ReverseRelation["ControlTypes"]

    class Meta:
        app = 'ervk'
        table = 'ctrl_levels'
        table_description = "Список уровней контроля"

class ControlTypes(Model):
    id = IntField(pk=True)
    uid = UUIDField(index=True, unqiue=True)
    title = CharField(max_length=255,unique=True, index=True)
    code = IntField(index=True)

    uid = ForeignKeyField('ervk.ControlLevel', related_name='levels', to_field='uid')

    class Meta:
        app = 'ervk'
        table = 'ctrl_types'
        table_description = 'Список типов контроля'


class ControlOrganizations(Model):
    id = IntField(pk=True)
    uid = UUIDField(index=True, unique=True)
    code = IntField(index=True)
    title = CharField(max_length=255, unique=True)
    code = IntField(index=True)
    ogrn = CharField(max_length=13, unique=True)
    
    uid = ForeignKeyField('ervk.ControlLevel', related_name='organizations', to_field='uid')

    class Meta:
        app = 'ervk'
        table = 'ctrl_orgs'
        table_description = 'Список контролирующих органов'

class ControlActions(Model):
    id = IntField(pk=True)
    uid = UUIDField(index=True, unique=True)
    code = IntField(index=True)
    title = CharField(index=True, max_length=255, unique=True)

    class Meta:
        app = 'ervk'
        table = 'ctrl_actions'
        table_description = 'Список контрольных действий'


class RiskCategories(Model):
    id = IntField(pk=True)
    uid = UUIDField(index=True, unqiue=True)
    limit = IntField()
    code = IntField()
    title = CharField(index=True, max_length=255, unique=True)
    
    class Meta:
        app = 'ervk'
        table = 'ctrl_risks'
        table_description = 'Категории рисков'

class ControlSubjects(Model):
    id = IntField(pk=True)
    code = IntField(index=True)
    title = CharField(max_length=255, unique=True, index=True)
    uid = UUIDField(index=True)

    class Meta:
        app = 'ervk'
        table = 'ctrl_subjects'
        table_description = 'Субъекты контроля'


__models__= [ControlLevel, ControlTypes, ControlOrganizations, ControlActions, RiskCategories, ControlSubjects]