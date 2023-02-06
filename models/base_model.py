from uuid import uuid4
from datetime import datetime
from . import storage # task 5
class BaseModel:
    def __init__(self, *args, ** kwargs):
        self.updated_at = datetime.now().isoformat()
        self.id = str(uuid4)
        self.created_at = datetime.now().isoformat()
    def save(self):
        self.updated_at = datetime.now().isoformat()
        storage.save() # task 5
    def to_json(self):
        pass
    def __str__(self):
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)
    def to_dict(self):
    # dictionary representation of instance attributes
        mydict = self.__dict__.copy() # task 3
        mydict["__class__"] = self.__class__.__name__ # task 4
        return mydict