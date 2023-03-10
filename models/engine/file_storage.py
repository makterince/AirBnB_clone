#!/usr/bin/python3
"""
This module defines a class FileStorage that serializes instances to a
JSON file and deserializes JSON file to instances
"""

import json
import os.path


class FileStorage:
    """serializes/deserializes instances to/from JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                json_dict = json.load(f)
                for key, value in json_dict.items():
                    cls = key.split(".")[0]
                    self.new(eval(cls)(**value))
