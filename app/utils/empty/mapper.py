from app.utils.core.mapper import Mapper
from app.utils.core.business_object import BusinessObject
from app.configs.base import db_connector

# from .business_object import DummyObject


class DummyMapper(Mapper):
    @staticmethod
    def find_all(cnx: db_connector) -> BusinessObject:
        pass

    @staticmethod
    def find_by_key(cnx: db_connector, key) -> BusinessObject:
        pass

    @staticmethod
    def insert(cnx: db_connector, object: BusinessObject) -> BusinessObject:
        pass

    @staticmethod
    def update(cnx: db_connector, object: BusinessObject) -> BusinessObject:
        pass

    @staticmethod
    def delete(cnx: db_connector, object: BusinessObject):
        pass
