from flask import Flask, render_template, redirect, url_for, session, make_response
from blueprints.products.product import product_page
from blueprints.supermarkets.supermarket import supermarket_page


app = Flask(__name__)
app.register_blueprint(product_page)
app.register_blueprint(supermarket_page)


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)