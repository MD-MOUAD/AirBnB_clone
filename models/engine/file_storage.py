#!/usr/bin/python3
""" The FileStorage class manages the storage and retrieval of data in
a file, as evident from the save, reload, and new methods"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ This method returns all the objects
        stored in the __objects dictionary.
        """
        return FileStorage.__objects

    def new(self, obj):
        """ This method adds a new object to the __objects dictionary.
        """
        key = obj.__class__.__name__ + '.' + obj.id
        # key = <class name>.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ This method writes the current data in the __objects
        dictionary to the JSON file.
        """
        data = {}
        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(data, f, indent=4)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
            for key, value in data.items():
                if "BaseModel" in key:
                    reloaded = BaseModel(**value)
                    self.new(reloaded)
                if "User" in key:
                    reloaded = User(**value)
                    self.new(reloaded)
                if "State" in key:
                    reloaded = State(**value)
                    self.new(reloaded)
                if "City" in key:
                    reloaded = City(**value)
                    self.new(reloaded)
                if "Amenity" in key:
                    reloaded = Amenity(**value)
                    self.new(reloaded)
                if "Place" in key:
                    reloaded = Place(**value)
                    self.new(reloaded)
                if "Review" in key:
                    reloaded = Review(**value)
                    self.new(reloaded)
        except Exception:
            pass
