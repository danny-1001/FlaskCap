import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__name__)) 
load_dotenv(os.path.join(basedir, '.env'))




class Config:
    SQLALCHEMY_DATABASE_URI = 'postgres://cueouoto:igoGF1rOlAF3KZd_xZtpcyRrHM8p73Sc@queenie.db.elephantsql.com:5432/cueouoto'
    SQLALCHEMY_TRACK_MODIFICATIONS= os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
