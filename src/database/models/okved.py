from uuid import uuid4
from tortoise.fields import IntField, UUIDField, TextField, CharField
from tortoise.fields.data import CharField
from tortoise.fields.relational import ReverseRelation, ForeignKeyField
from tortoise.models import Model

# Раздел    

class Chapters(Model):
    id = IntField(pk=True)
    guid = UUIDField(default=uuid4, unique=True)
    code = CharField(max_length=5, index=True)
    title = TextField()

    groups:ReverseRelation['Groups']

    class Meta:
        app ='okved'
        table='okved_chapters'

class Groups(Model):
    id = IntField(pk=True)
    guid = UUIDField(default=uuid4, unique=True)
    code = CharField(max_length=5, index=True)
    title = TextField()

    chapters = ForeignKeyField(model_name='okved.Chapters', related_name='chapters',to_field='guid')
    subgroups:ReverseRelation["SubGroups"]

    class Meta:
        app ='okved'
        table='okved_groups'

class SubGroups(Model):
    id = IntField(pk=True)
    guid = UUIDField(default=uuid4, unique=True)
    code = CharField(max_length=10, index=True)
    title = TextField()

    groups = ForeignKeyField(model_name='okved.Groups', related_name='subgroups', to_field='guid')

    class Meta:
        app ='okved'
        table='okved_subgroups'

__models__= [Chapters, Groups, SubGroups]