"""Main application entry point."""
from flask import Flask
from flask_login import LoginManager
from extensions import db
from routes.main import main
from routes.auth import auth
from models import User

app = Flask(__name__)

# 基本配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 'your-secret-key'

# 初始化扩展
db.init_app(app)

# 设置 Flask-Login
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
    app.run(debug=True)