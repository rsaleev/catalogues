from typing import Union, List, Any, Type

from datetime import date

from tortoise.models import Model as ORMModel
from tortoise.functions import Max


def format_date(value:Union[date,None])->str:
    """format_date 

    Args:
        value (Union[datetime,None]): значение даты

    Returns:
        str: форматированное значение в строку или пустая строка
    """
    if not value:
        return ''
    else:
        return value.strftime('%d-%m-%Y')

def format_array(value:List[Any],sep=' ')->str:
    """format_array


    Args:
        value (List[Any]): массив значений (list)

    Returns:
        str: контатенированная строка
    """
    return sep.join(value)


async def recalc_pk(model:ORMModel):
    """
    recalc_index 

    Изменение текущего значения первичного ключа

    Args:
        model (ORMModel): модель TortoiseORM
    """
    vals=await model.all()
    table = model.Meta.table #type: ignore
    max_pk = max(v.pk for v in vals)
    await model.raw(f"ALTER SEQUENCE {table}_id_seq RESTART WITH {max_pk};")

       
