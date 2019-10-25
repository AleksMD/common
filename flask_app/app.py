from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/fruits')
def fruits():
    fruits_db = ['melon', 'apple', 'strawberry', 'grape']
    return render_template('fruits.html', fruits=fruits_db)


@app.route('/vegetables')
def vegetables():
    vegetables_db = ['beans', 'carrot', 'beetroot', 'cucumber']
    return render_template('vegetables.html', vegetables=vegetables_db)


if __name__ == '__main__':
    app.run(debug=True)
