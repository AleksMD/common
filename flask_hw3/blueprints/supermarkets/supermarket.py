from flask import Blueprint, render_template


supermarket_page = Blueprint('supermarket_page', __name__, template_folder='./templates')


@supermarket_page.route('/supermarket', methods=['GET', 'POST'])
@supermarket_page.route('/supermarket/<id>', methods=['GET'])
def supermarket(id=None):
    return render_template('supermarket.html')
