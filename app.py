from flask import Flask
from flask_pymongo import PyMongo
from config.config import Config
from controller.user_controller import user_controller
from controller.transaction_controller import transaction_controller

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database (MongoDB)
mongo = PyMongo(app)

# Register the controllers (blueprints)
app.register_blueprint(user_controller, url_prefix='/api')
app.register_blueprint(transaction_controller, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
