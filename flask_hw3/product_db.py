from itertools import count


id_products_gen = count(0)
id_supermarket_gen = count(0)


class ProductTemplate:
    """
    Is used to produce a new product instance to store in PRODUCT_DB
    """
    def __init__(self, name: str, description: str, img_name: str, price: int, category: str = None):
        self.category = category
        self.id = next(id_products_gen)
        self.name = name
        self.description = description
        self.img_name = img_name
        self.price = price

    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if key != 'category'}


PRODUCT_DB = {'fruits': [{'id': next(id_products_gen), 'name': 'Apples',
                          'description': 'Fresh ripe apples from Ukrainian gardens',
                          'img_name': 'apples.jpg', 'price': 15},
                         {'id': next(id_products_gen), 'name': 'Bananas',
                          'description': 'Bananas were grown and delivered from Ecuador',
                          'img_name': 'bananas.jpg', 'price': 15}],

              'vegetables': [{'id': next(id_products_gen), 'name': 'Carrot',
                              'description': 'Carrot was grown and delivered from the USA.',
                              'img_name': 'carrot.jpg', 'price': 15},
                             {'id': next(id_products_gen), 'name': 'Tomatoes',
                              'description': 'Tomatoes were grown and delivered from Poland',
                              'img_name': 'tomatoes.jpg', 'price': 23}],
              'other': []

              }

SUPERMARKET_DB = {}
