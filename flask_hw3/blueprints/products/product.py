from flask import Blueprint, render_template, request, session, jsonify
from product_db import PRODUCT_DB, ProductTemplate


product_page = Blueprint('product_page', __name__, template_folder='./templates')


@product_page.route('/product/<int:id_>', methods=['GET'])
def product(id_=None):
    if request.method == 'GET' and id_ is None:
        return render_template('all_products.html')
    elif request.method == 'GET' and id_ is not None:
        required_product = {key: value for category in PRODUCT_DB.values()
                            for item in category for key, value in item.items()
                            if item.get('id') == id_}
        return required_product


@product_page.route('/product', methods=['POST', 'GET'])
def get_or_update_product():
    if request.method == 'POST':
        product_to_add = ProductTemplate(**request.form)
        category = product_to_add.category
        if category is not None and category in PRODUCT_DB:
            PRODUCT_DB[category].append(product_to_add.to_dict())
        elif category is not None and category not in PRODUCT_DB:
            PRODUCT_DB[category] = [product_to_add.to_dict()]
        else:
            PRODUCT_DB['other'].append(product_to_add.to_dict())
        return 'Successfully added'
    elif request.method == 'GET':
        data = request.form
        response = []
        if data:
            for item in data.items():
                key, value = item
            for category in PRODUCT_DB.values():
                for item in category:
                    if not isinstance(value, type(item.get(key))):
                        try:
                            value = type(item.get(key))(value)
                            if item.get(key) == value:
                                response.append(item)
                        except (TypeError, ValueError):
                            return 'You have entered bad value'
            return jsonify(tuple(response))
        else:
            return render_template('all_products.html', data=PRODUCT_DB)
    else:
        return 'Bad request'
