import os

from flask import Blueprint, render_template, request, session, url_for, redirect, flash
from werkzeug.utils import secure_filename

from supermarket_db import SUPERMARKET_DB, SupermarketTemplate

supermarket_page = Blueprint('supermarket_page', __name__,
                             template_folder='./templates',
                             static_folder='static',
                             static_url_path='/supermarkets')


@supermarket_page.route('/supermarket', methods=['GET', 'POST'])
def get_or_update_supermarket():
    if request.method == 'POST':
        client_form = request.form
        received_file = request.files['supermarket_img']
        filename = secure_filename(received_file.filename)
        if client_form:
            product_to_add = SupermarketTemplate(img_name=filename, **client_form)
            SUPERMARKET_DB.append(product_to_add)
            received_file.save(os.path.join(f'{supermarket_page.root_path}/static/', filename))
            return redirect(url_for('home'))
        else:
            return redirect(url_for('home'))
    elif request.method == 'GET':
        id_ = request.args.get('id')
        if id_:
            session[id_] = True
            required_sup = [item.to_dict() for item in SUPERMARKET_DB if item.id == id_]
            if len(required_sup) == 1:
                return render_template('supermarket.html',  sup=required_sup[0])
            else:
                flash('Unfortunately supermarket was not founded. Please try another one!')
                return render_template('all_supermarkets.html')
        data = request.args
        if data:
            response = {sup for item in data.items()
                        for sup in SUPERMARKET_DB if item in sup}
            if response:
                return render_template('all_supermarkets.html', link_flags=session, data=response)
            else:
                flash('Unfortunately supermarket was not founded. Please try another one!')
                return render_template('all_supermarkets.html')
        else:
            data = [sup.to_dict() for sup in SUPERMARKET_DB]
            return render_template('all_supermarkets.html', link_flags=session, data=data)


@supermarket_page.route('/add_supermarket', methods=['GET'])
def add_supermarket():
    return render_template('add_supermarket.html')
