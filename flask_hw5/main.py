from flask import Flask

from create_tables import create_tables
from blueprints.rooms import rooms_page
from blueprints.staff import staff_page
from blueprints.tenants import tenants_page
from config import get_config
from hotel_db import DB

app = Flask(__name__)

for conf in get_config():
    app.config.from_object(conf)
DB.init_app(app)
app.register_blueprint(create_tables)
app.register_blueprint(rooms_page)
app.register_blueprint(staff_page)
app.register_blueprint(tenants_page)


if __name__ == '__main__':
    app.run()
