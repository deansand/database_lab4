from my_project.auth.domain.i_dto import ItemDTO
from my_project import db

class GeneralDAO:
    def get_all_items(self):
        # Query the database to get all items
        items = db.session.query(ItemDTO).all()
        return [item.to_dict() for item in items]

    def create_item(self, data):
        # Insert a new item into the database
        item = ItemDTO(**data)
        db.session.add(item)
        db.session.commit()
        return item.to_dict()