from flask import Blueprint, render_template, request, session


product_page = Blueprint('product_page', __name__, template_folder='./templates')


@product_page.route('/product', methods=['GET', 'POST'])
@product_page.route('/product/<id_:int>', methods=['GET'])
def product(id_=None):
    if 
    return render_template('product.html')