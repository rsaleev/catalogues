from uuid import UUID, uuid4

from tortoise.fields.data import BooleanField, CharField, DatetimeField, FloatField
from tortoise.models import Model
from tortoise.fields import IntField, TextField, UUIDField
from tortoise.fields.relational import OneToOneField, ReverseRelation, ForeignKeyField

from custom_fields import TextArrayField

class Codex(Model):

    id = IntField(pk=True)
    full = CharField(max_length=200, unique=True, description='Полное название')
    short = CharField(max_length=10, unique=True, description='Краткое название')
    guid = UUIDField(default=uuid4, unique=True, index=True, description='Уникальный идентификатор')
    updated = DatetimeField(auto_now=True)

    articles: ReverseRelation['Article']

    class Meta:
        app ='codex'
        table_name ='codexes'
        ordering=["id"]


class Article(Model):

    id = IntField(pk=True)
    number = CharField(10, unique=True)
    title = TextField()
    guid = UUIDField(default=uuid4, unique=True, index=True)
    updated = DatetimeField(auto_now=True)

    paragraphs:ReverseRelation['Paragraph']

    codex = OneToOneField('codexes.Codexes', related_name='codex', to_field='guid', through='article_codex')

    def __hash__(self) -> int:
        return hash((str(self.title), str(self.number)))

    class Meta:
        app ='codex'
        table_name ='articles'
        ordering=["id"]


    class PydanticMeta:
        exclude=("id","guid", "codex_id")

class Paragraph(Model):

    id = IntField(pk=True)
    idx = IntField()
    content = TextField()
    updated = DatetimeField(auto_now=True)
    keywords = TextArrayField()
    
    article = ForeignKeyField('codexes.Articles', related_name='paragraphs', to_field='guid', through='paragraph_article')

    def __hash__(self) -> int:
        return hash((str(self.content),str(self.idx)))

    class Meta:
        app ='codex'
        table_name ='articles'
        ordering=["id"]

    class PydanticMeta:
        exclude=("id","article_id")

class Sanction(Model):

    id = IntField(pk=True)
    title = CharField(max_length=255, null=False, unique=True)
    min_val = FloatField()
    max_val = FloatField()
    measure = IntField()
    physical = BooleanField(default=False)
    juristic = BooleanField(default=False)
    executive = BooleanField(default=False)
    selfemployed = BooleanField(default=False)
    guid = UUIDField(null=False, default=uuid4, unique=True)

    article = ForeignKeyField('codexes.Articles', related_name='sactions', to_field='guid', through='sanction_article')

    class Meta:
        app ='codex'
        table_name ='sanctions'
        ordering=["id"]


    class PydanticMeta:
        exclude=("id","article_id", "guid")

__models__ = [Codex, Article, Paragraph, Sanction]