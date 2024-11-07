from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class ClientType(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "client_type"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type: str = db.Column(db.String(30))

    def __repr__(self) -> str:
        return f"ClientType({self.id}, '{self.type}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "type": self.type,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ClientType:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = ClientType(**dto_dict)
        return obj
    
    @staticmethod
    def get_all():
        """
        Gets all ClientType objects from database table using Service layer as DTO objects.
        :return: list of all objects as DTOs
        """
        return ClientType.query.all()
    
    @staticmethod
    def delete_by_id(id: int):
        """
        Deletes ClientType object from database table by id.
        :param id: id value
        """
        ClientType.query.filter(ClientType.id == id).delete()
        db.session.commit()