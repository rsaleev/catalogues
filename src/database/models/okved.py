from uuid import uuid4
from tortoise.fields import IntField, UUIDField, TextField, CharField
from tortoise.fields.data import CharField
from tortoise.fields.relational import ReverseRelation, ForeignKeyField
from tortoise.models import Model

__title__ = "Справочник ОКВЭД"

class OkvedBase(Model):
    id = IntField(pk=True, description='Первичный ключ')
    guid = UUIDField(default=uuid4, unique=True, description='Уникальный идентификатор')
    code = CharField(max_length=255, index=True,  description='Уникальный код')
    title = TextField(description='Описание')

    class Meta:
        abstract=True

class OkvedChapter(OkvedBase):
    
    groups:ReverseRelation['OkvedGroup']

    class Meta:
        app ='okved'
        table='okved_chapters'
        table_description = "Раздел ОКВЭД"
        ordering = ["id"]

class OkvedGroup(OkvedBase):
    id = IntField(pk=True)
    guid = UUIDField(default=uuid4, unique=True)
    code = CharField(max_length=5, index=True)
    title = TextField()
   
    chapters = ForeignKeyField(model_name='okved.OkvedChapter', related_name='chapters',to_field='guid')
    subgroups:ReverseRelation["OkvedSubGroup"]

    class Meta:
        app ='okved'
        table='okved_groups'
        table_description = "Группа ОКВЭД"
        ordering = ["id"]

class OkvedSubGroup(OkvedBase):
   
    code = CharField(max_length=10, index=True)
    title = TextField()

    groups = ForeignKeyField(model_name='okved.OkvedGroup', related_name='subgroups', to_field='guid')

    class Meta:
        app ='okved'
        table='okved_subgroups'
        table_description = "Раздел ОКВЭД"
        ordering = ["id"]


__models__= [OkvedChapter, OkvedGroup, OkvedSubGroup]