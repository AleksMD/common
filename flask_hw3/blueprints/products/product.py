import os

from flask import Blueprint, render_template, request, session, url_for, redirect, flash
from werkzeug.utils import secure_filename

from product_db import PRODUCT_DB, ProductTemplate

product_page = Blueprint('product_page', __name__, template_folder='./templates', static_folder='static',
                         static_url_path='/products')


@product_page.route('/product', methods=['GET', 'POST'])
def get_or_update_product():
    if request.method == 'POST':
        client_form = request.form
        received_file = request.files['product_img']
        filename = secure_filename(received_file.filename)
        if client_form:
            product_to_add = ProductTemplate(img_name=filename, **client_form)
            PRODUCT_DB.append(product_to_add)
            received_file.save(os.path.join(f'{product_page.root_path}/static/', filename))
            return redirect(url_for('home'))
        else:
            return redirect(url_for('home'))
    elif request.method == 'GET':
        id_ = request.args.get('id')
        if id_:
            session[id_] = True
            required_product = [item.to_dict() for item in PRODUCT_DB if item.id == id_]
            if len(required_product) == 1:
                return render_template('product.html',  prod=required_product[0])
            else:
                flash('Unfortunately the product was not founded. Please try another one!')
                return render_template('all_products.html')
        data = request.args
        if data:
            response = {prod for item in data.items()
                        for prod in PRODUCT_DB if item in prod}
            if response:
                return render_template('all_products.html', link_flags=session, data=response)
            else:
                flash('Unfortunately the product was not founded. Please try another one!')
                return render_template('all_products.html')
        else:
            data = [prod.to_dict() for prod in PRODUCT_DB]
            return render_template('all_products.html', data=data, link_flags=session)


@product_page.route('/add_product', methods=['GET'])
def add_product():
    return render_template('add_product.html')
