import os

from flask import Blueprint, render_template, request, jsonify, url_for, redirect
from werkzeug.utils import secure_filename

from product_db import PRODUCT_DB, ProductTemplate

product_page = Blueprint('product_page', __name__, template_folder='./templates', static_folder='static',
                         static_url_path='/products')


@product_page.route('/product', methods=['GET', 'POST'])
def get_or_update_product():
    if request.method == 'POST':
        form = request.form
        file = request.files['product_img']
        filename = secure_filename(file.filename)
        if form:
            product_to_add = ProductTemplate(img_name=filename, **form)
            PRODUCT_DB.append(product_to_add)
            file.save(os.path.join(product_page.root_path + '/static/', filename))
            return redirect(url_for('home'))
        else:
            return redirect(url_for('home'))
    elif request.method == 'GET':
        id_ = request.args.get('id')
        if id_ is not None:
            required_product = [item.to_dict() for item in PRODUCT_DB if item.id == id_]
            if len(required_product) == 1:
                return render_template('product.html',  prod=required_product[0])
            elif len(required_product) > 1:
                return render_template('all_products.html', data=required_product)
            else:
                return 'Product was not founded!'
        data = request.form
        if data:
            response = [prod.to_dict() for item in data.items()
                        for prod in PRODUCT_DB if item in prod]
            return jsonify(response)
        else:
            data = [prod.to_dict() for prod in PRODUCT_DB]
            return render_template('all_products.html', data=data)


@product_page.route('/add_product', methods=['GET'])
def add_product():
    return render_template('add_product.html')
