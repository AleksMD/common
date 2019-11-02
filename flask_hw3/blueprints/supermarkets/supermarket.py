import os

from flask import Blueprint, render_template, request, jsonify, url_for, redirect
from werkzeug.utils import secure_filename

from supermarket_db import SUPERMARKET_DB, SupermarketTemplate

supermarket_page = Blueprint('supermarket_page', __name__,
                             template_folder='./templates',
                             static_folder='static',
                             static_url_path='/supermarkets')


@supermarket_page.route('/supermarket', methods=['GET', 'POST'])
def get_or_update_supermarket():
    if request.method == 'POST':
        form = request.form
        file = request.files['supermarket_img']
        filename = secure_filename(file.filename)
        if form:
            product_to_add = SupermarketTemplate(img_name=filename, **form)
            SUPERMARKET_DB.append(product_to_add)
            file.save(os.path.join(supermarket_page.root_path + '/static/', filename))
            return redirect(url_for('home'))
        else:
            return redirect(url_for('home'))
    elif request.method == 'GET':
        id_ = request.args.get('id')
        data = request.args
        if id_:
            print('inside id')
            required_sup = [item.to_dict() for item in SUPERMARKET_DB if item.id == id_]
            if len(required_sup) == 1:
                return render_template('supermarket.html',  sup=required_sup[0])
            elif len(required_sup) > 1:
                return render_template('all_supermarkets.html', data=required_sup)
            else:
                return 'Supermarket was not founded with this id!'
        elif not id_ and data:
            response = {sup for item in data.items()
                        for sup in SUPERMARKET_DB if item in sup}
            return render_template('all_supermarkets.html', data=response)
        else:

            data = [sup.to_dict() for sup in SUPERMARKET_DB]
            return render_template('all_supermarkets.html', data=data)


@supermarket_page.route('/add_supermarket', methods=['GET'])
def add_supermarket():
    return render_template('add_supermarket.html')
