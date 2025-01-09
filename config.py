import os

class Config:
    SECRET_KEY = 'dev'
    
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database', 'app.db')
    
    SQLALCHEMY_BINDS = {
        'contact': 'sqlite:///' + os.path.join(basedir, 'database', 'contact.db')
    }
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False