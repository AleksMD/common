from flask import Flask
from config import get_config
from blueprints.rooms import rooms_page

app = Flask(__name__)
app.config.from_object(get_config())
app.register_blueprint(rooms_page)

if __name__ == '__main__':
    app.run()