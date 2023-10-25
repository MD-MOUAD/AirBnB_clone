#!/usr/bin/python3
""" BaseModel is a class that encapsulates shared attributes and methods,
serving as a blueprint for other classes. It manages the initialization,
serialization, and deserialization of future instances, ensuring consistent
handling of these aspects.
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    class BaseModel that defines all common
    attributes/methods for other classes
    """
    def __init__(self):
        """Constructor for the BaseModel class.
        Args:
            *args: Variable number of positional arguments.
            **kwargs: Keyword arguments.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: A string containing the class name, the object's ID, and its
            attributes.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at attribute with the current timestamp.

        Returns:
            None
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the object.

        Returns:
            dict: A dictionary containing the object's attributes and the
            "__class__" key with the class name. Datetime objects are
            converted to ISO formatted strings.
        """
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = datetime.isoformat(self.created_at)
        dictionary["updated_at"] = datetime.isoformat(self.updated_at)
        return dictionary
