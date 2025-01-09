
import os
from datetime import datetime, UTC
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
                title='Personal Works Website',
                description='A modern portfolio website built with Flask and SQLAlchemy. Features include project showcasing, user authentication, and a comment system.',
                image_url='static/images/projects/1.jpg',
                documentation_url='static/files/1.zip',
                video_url='static/videos/1.mp4',
                github_url='https://gitlab.com/web4383802/web.git',
                category='Web Development',
                technologies='Python,Flask,HTML,CSS,JavaScript',
                
            ),
            Project(
                title='Quiz System',
                description='An interactive quiz system developed using Python. Includes features for both students and teachers, with real-time scoring and progress tracking.',
                image_url='static/images/projects/2.jpg',
                documentation_url='static/files/2.zip',
                video_url='static/videos/2.mp4',
                github_url='https://gitlab.com/web4383802/quiz.git',
                category='Desktop Application',
                technologies='Python,Tkinter,SQLite,Pandas',
             
            ),
            Project(
                title='iPhone Application Design',
                description='A simple personal website based on HTML and CSS',
                image_url='static/images/projects/3.jpg',
                documentation_url='static/files/3.zip',
                video_url='static/videos/3.mp4',
                github_url='https://gitlab.com/web4383802/app-design.git',
                category='UI/UX Design',
                technologies='Figma,UI Design,UX Design',
              
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
