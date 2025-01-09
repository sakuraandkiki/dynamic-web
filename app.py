import os
from flask import Flask
from flask_login import LoginManager
from extensions import db
from routes.main import main
from routes.auth import auth
from models import User

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 'your-secret-key'


db.init_app(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


app.register_blueprint(main)
app.register_blueprint(auth, url_prefix='/auth')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    if os.getenv('OPENSHIFT_DEPLOYMENT'):
    
        app.run(host='0.0.0.0', port=8080, debug=True)
    else:
        
        app.run(debug=True)
