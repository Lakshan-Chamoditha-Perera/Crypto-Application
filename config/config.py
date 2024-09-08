import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URI',
        'mysql+pymysql://root:1234@db:3306/crypto'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
