import json

from flask import Blueprint, render_template, request, session, jsonify
from product_db import PRODUCT_DB, ProductTemplate

product_page = Blueprint('product_page', __name__, template_folder='./templates')


@product_page.route('/product', methods=['GET', 'POST'])
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
        id_ = request.args.get('id_')
        if id_ is not None:
            required_product = [item for products in PRODUCT_DB.values()
                                for item in products if item.id == id_]
            if required_product:
                return render_template('product.html', title=required_product[0].category,
                                       data=required_product[0].to_dict())
            else:
                return 'Product was not founded!'
        data = request.form
        response = []
        if data:
            category_to_search = PRODUCT_DB.get(data['category'])
            for item in data.items():
                for prod in category_to_search:
                    if item in prod:
                        response.append(prod.to_dict())
            return json.dumps(response)
        else:
            return render_template('all_products.html', data=PRODUCT_DB)
