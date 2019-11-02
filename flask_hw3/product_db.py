import json
import uuid


class ProductTemplate:
    """
    Is used to produce a new product instance to be stored in the PRODUCT_DB
    """
    def __init__(self,
                 name: str,
                 description: str,
                 img_name: str,
                 price: int,
                 category: str = None):

        self.category = category
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.img_name = img_name
        self.price = price

    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if key != 'category'}

    def to_json(self):
        return json.dumps(self.to_dict())

    def __contains__(self, item):
        if isinstance(item, tuple) and len(item) == 2:
            return item in self.__dict__.items()
        else:
            return NotImplemented


PRODUCT_DB = [ProductTemplate('Apples', 'Fresh ripe apples from Ukrainian gardens',
                              'apples.jpg', 15, category='fruits'),
              ProductTemplate('Bananas', 'Bananas were grown and delivered from Ecuador',
                              'bananas.jpg', 15, category='fruits'),
              ProductTemplate('Carrot', 'Carrot was grown and delivered from the USA.',
                              'carrots.jpg', 15, category='vegetables'),
              ProductTemplate('Tomatoes', 'Tomatoes were grown and delivered from Poland',
                              'tomatoes.jpg', 23, category='vegetables')]


