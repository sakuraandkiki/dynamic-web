
import os
from flask import Flask
from flask_login import LoginManager
from extensions import db
from routes.main import main
from routes.auth import auth
from models import User, Project

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

with app.app_context():
    db.create_all()
    if not Project.query.first():  
        projects = [
            Project(
                title='Dynamic Website',
                description='A personal portfolio website built with Flask and SQLAlchemy. Features include project showcasing, user authentication, and a comment system.',
                image_url='project1.jpg',
                github_url='https://github.com/sakuraandkiki/dynamic-web',
                category='Web Development',
                technologies='Python, Flask, SQLAlchemy, Bootstrap'
            ),
            Project(
                title='E-commerce Platform',
                description='An online shopping platform with product management, shopping cart, and payment integration.',
                image_url='project2.jpg',
                github_url='https://github.com/yourusername/ecommerce',
                category='Web Application',
                technologies='Python, Django, React, PostgreSQL'
            ),
            Project(
                title='Task Management System',
                description='A collaborative task management system with real-time updates and team features.',
                image_url='project3.jpg',
                github_url='https://github.com/yourusername/taskmanager',
                category='Web Application',
                technologies='Python, Flask, Socket.IO, MongoDB'
            )
        ]
        for project in projects:
            db.session.add(project)
        db.session.commit()

app.register_blueprint(main)
app.register_blueprint(auth, url_prefix='/auth')

if __name__ == '__main__':
    if os.getenv('OPENSHIFT_DEPLOYMENT'):
        app.run(host='0.0.0.0', port=8080, debug=True)
    else:
        app.run(debug=True)
