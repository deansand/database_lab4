from sqlalchemy import Column, Integer, String
from my_project import db

class IDto:
    def to_dict(self):
        raise NotImplementedError

class ItemDTO(db.Model, IDto):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }