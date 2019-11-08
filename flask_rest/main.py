from flask import Flask
from config import get_config
from blueprints.rooms import rooms_page
from blueprints.staff import staff_page


app = Flask(__name__)
app.config.from_object(get_config())
app.register_blueprint(rooms_page)
app.register_blueprint(staff_page)

if __name__ == '__main__':
    app.run()
