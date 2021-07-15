from .dict import DictDatabase
from typing import Union
try:
    from .mongo import MongoDatabase
    DataBase = Union[DictDatabase, MongoDatabase]
except ImportError:
    DataBase = DictDatabase

 