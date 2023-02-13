#!/usr/bin/python3
"""
    Define class FileStorage
"""
import json
import models


class FileStorage:
    """
        Serializes instances to JSON file and deserializes to JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            Return the dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        Set new obj into __objects
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        """
        Serializes the objects into JSON file
        """
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        """
        Reload the file and deserializes JSON into __objects
        """

        try:
            with open(FileStorage.__file_path, mode='r') as fd:
                objects_dict = json.load(fd)

            for key, value in objects_dict.items():
                class_name = value.get('__class__')
                obj = eval(class_name + '(**value)')
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
