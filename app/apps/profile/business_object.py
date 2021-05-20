from app.utils.core.business_object import BusinessObject


class ProfileObject(BusinessObject):
    def __init__(self, interests: str, type_: str, online: bool,
                 frequency: int, expertise: str, extroversion: str,
                 id_: int = 0):
        self.interests = interests
        self.type_ = type_
        self.online = online
        self.frequency = frequency
        self.expertise = expertise
        self.extroversion = extroversion
        super().__init__(id_=id_)