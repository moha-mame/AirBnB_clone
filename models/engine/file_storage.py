import json
class FileStorage:
    __file_path=""
    __objects={}
    def __init__(self, *args, **kwargs): # * args:- tuple(must be ordered) ** kwargs:- dictionary(order is not mandatory)
        pass
    def all(self):
        return self.__objects
    def new(self, obj):
        self.__objects = obj
    def save(self): # serializes python object to json string : json.dumps(object)
        json.dumps(self.__objects)
    def reload(self): # deserializes from json string to python object : json.loads(string)
        json.loads(self.__objects)
