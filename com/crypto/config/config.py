import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+pymysql://username:password@localhost/db_name')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
