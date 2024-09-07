from flask import Flask
from com.crypto.models.models import db
from com.crypto.config.config import Config
from controller.user_controller import user_controller
from controller.transaction_controller import transaction_controller
import pymysql

# Use PyMySQL to act as MySQLdb
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Register the controllers (blueprints)
app.register_blueprint(user_controller, url_prefix='/api')
app.register_blueprint(transaction_controller, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
