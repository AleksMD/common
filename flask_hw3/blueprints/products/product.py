from flask import Blueprint, render_template


product_page = Blueprint('product_page', __name__, template_folder='./templates')


@product_page.route('/product', methods=['GET', 'POST'])
@product_page.route('/product/<id>', methods=['GET'])
def product(id=None):
    return render_template('product.html')