#!/usr/bin/python3
"""
    Defines the common attributes/methods for other classes
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """ base class for all models in this project """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.
        If kwargs is not empty:
            each key of this dictionary is an attribute name
            each value of this dictionary is the value of this attribute name
            created_at and updated_at are strings in this dictionary,
            but inside your BaseModel instance is working with datetime object.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.datetime.strptime(value,
                                                       '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)
            self.id = kwargs["id"] if "id" in kwargs else str(uuid.uuid4())
            self.created_at = kwargs["created_at"]
            if "created_at" in kwargs else datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ String representation of the class BaseModel """

        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ Updates the public instance attribute updated_at with
            the current datetime
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
            Returns a dictionary containing all keys/values
            of __dict__ of the instance
        """
        my_dict = copy.deepcopy(self.__dict__)
        my_dict['__class__'] = type(self).__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
