from my_project.auth.dao.general_dao import GeneralDAO

class GeneralService:
    def __init__(self):
        self.dao = GeneralDAO()

    def get_all_items(self):
        return self.dao.get_all_items()

    def create_item(self, data):
        return self.dao.create_item(data)

    # Add more methods for update and delete operations