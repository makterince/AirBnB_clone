#!/usr/bin/python3
"""
    Defines the common attributes/methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """ base class for all models in this project """
    
    def init(self):
        """
        Constructor of the class BaseModel
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ String representation of the class BaseModel """
        
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                self.__dict__)

    def save(self):
        """ Updates the public instance attribute updated_at with
            the current datetime
        """
        
        self.updated_at = datetime.now()
    
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
