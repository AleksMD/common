import json
import uuid


class SupermarketTemplate:
    """
    Is used to produce a new supermarket instance to be stored in the SUPERMARKET_DB
    """
    def __init__(self,
                 name: str,
                 location: str,
                 img_name: str):

        self.id = str(uuid.uuid4())
        self.name = name
        self.location = location
        self.img_name = img_name

    def to_dict(self):
        return {key: value for key, value in self.__dict__.items()}

    def to_json(self):
        return json.dumps(self.to_dict())

    def __contains__(self, item):
        if isinstance(item, tuple) and len(item) == 2:
            return item in self.__dict__.items()
        else:
            return NotImplemented


SUPERMARKET_DB = [SupermarketTemplate('Billa', 'Odessa',
                                      'billa.jpg'),
                  SupermarketTemplate('Class', 'Lviv',
                                      'class.jpg'),
                  SupermarketTemplate('Rost', 'Kharkiv',
                                      'rost.jpg')
                  ]
