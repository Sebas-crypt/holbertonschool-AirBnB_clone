from uuid import uuid4
from datetime import datetime

class BaseModel:
    """BaseModel class defining common attributes/methods for other classes.

    Public instance attributes:
        id: string - assigned with a uuid when an instance is created
        created_at: datetime - assigned with the current datetime when an instance is created
        updated_at: datetime - assigned with the current datetime when an instance is created and
                                 updated every time you change your object

    Public instance methods:
        __str__: prints [<class name>] (<self.id>) <self.__dict__>
        save(self): updates the public instance attribute updated_at with the current datetime
        to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance:
            by using self.__dict__, only instance attributes set will be returned
            a key __class__ must be added to this dictionary with the class name of the object
            created_at and updated_at must be converted to string object in ISO format:
                format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
                you can use isoformat() of datetime object
            This method will be the first piece of the serialization/deserialization process:
            create a dictionary representation with “simple object type” of our BaseModel

    """

    def __init__(self, *args, **kwargs):
        """Initialize public instance attributes."""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.utcnow()
        else:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key == 'id':
                    setattr(self, key, str(value))
                else:
                    setattr(self, key, value)

    def __str__(self):
        """Return a string representation of the class."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute updated_at with the current datetime."""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict
