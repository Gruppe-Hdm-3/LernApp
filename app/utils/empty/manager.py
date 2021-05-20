from .mapper import DummyM
from .business_object import DummyObject
from app.configs.base import db_connector


class DummyManager:
    """Dummy Manager class. For managing database interactions."""

    @staticmethod
    def insert_dummy(dummy: DummyObject) -> DummyObject:
        """Insert Dummy Manager."""
        with db_connector as db:
            cnx = db._cnx
            return DummyM.insert(cnx=cnx, object=dummy)
