#!/usr/bin/python3

"""
    import uuid for unique id and datetime for time and date
"""
import uuid
import datetime


class BaseModel:
    """
        class BaseModel that defines all common attributes/methods for other classes
    """
    def __init__(self):
        """
            Initializes a new instance of the BaseModel class.
        """
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.id = str(uuid.uuid4())

    def __str__(self):
        """
            Returns a string representation of the BaseModel object
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
            Updates the public instance attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
            Returns a dictionary containing all keys/values of __dict__ of the instance

            Returns:
                dict: A dictionary containing all instance attributes.
        """
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
