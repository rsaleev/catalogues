from typing import Optional, List, Dict, Any



from pydantic import BaseModel


"""
https://tortoise-orm.readthedocs.io/en/latest/models.html

describe(serializable)

{
    "name":                 str     # Qualified model name
    "app":                  str     # 'App' namespace
    "table":                str     # DB table name
    "abstract":             bool    # Is the model Abstract?
    "description":          str     # Description of table (nullable)
    "docstring":            str     # Model docstring (nullable)
    "unique_together":      [...]   # List of List containing field names that
                                    #  are unique together
    "pk_field":             {...}   # Primary key field
    "data_fields":          [...]   # Data fields
    "fk_fields":            [...]   # Foreign Key fields FROM this model
    "backward_fk_fields":   [...]   # Foreign Key fields TO this model
    "o2o_fields":           [...]   # OneToOne fields FROM this model
    "backward_o2o_fields":  [...]   # OneToOne fields TO this model
    "m2m_fields":           [...]   # Many-to-Many fields
}

"""


class ORMModelDescription(BaseModel):
    app:str
    table:str
    abstract:bool
    description:Optional[str]


class CatalogueTable(BaseModel):
    table:str
    description:Optional[str] = ''


    class Meta:
        exclude =['abstact']

class CatalogueName(BaseModel):
    title:str 
    data:List[CatalogueTable]


class Catalogues(BaseModel):
    catalogues:List[CatalogueName]
