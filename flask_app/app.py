from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/fruits')
def fuits():
    fruits = ['melon', 'apple', 'strawberry', 'grape']
    return render_template('fruits.html', fruits=fruits)

@app.route('/vegetables')
def vegetables():
    vegetables = ['beans', 'carrot', 'beetroot', 'cucumber']
    return render_template('vegetables.html', vegetables=vegetables)


if __name__ == '__main__':
    app.run(debug=True)