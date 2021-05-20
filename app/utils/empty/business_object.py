from app.utils.core.business_object import BusinessObject


class DummyObject(BusinessObject):
    def __init__(self, name: str, id_: int = 0):
        self.name = name
        super().__init__(id_=id_)
