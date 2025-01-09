from app import app, db
from models import Project, Comment, User
from datetime import datetime

def init_db():
    with app.app_context():
        
        db.drop_all()
        db.create_all()

       
        projects = [
            Project(
                title='Personal Works Website',
                description='A modern portfolio website built with Flask and SQLAlchemy. Features include project showcasing, user authentication, and a comment system.',
                image_url='static/images/projects/1.jpg',
                documentation_url='static/docs/project1.pdf',
                video_url='static/videos/1.mp4',
                github_url='https://gitlab.com/web4383802/web.git',
                category='Web Development',
                technologies='Python,Flask,HTML,CSS,JavaScript',
                created_at=datetime.utcnow()
            ),
            Project(
                title='Quiz System',
                description='An interactive quiz system developed using Python. Includes features for both students and teachers, with real-time scoring and progress tracking.',
                image_url='static/images/projects/2.jpg',
                documentation_url='static/docs/project2.pdf',
                video_url='static/videos/2.mp4',
                github_url='https://gitlab.com/web4383802/quiz.git',
                category='Desktop Application',
                technologies='Python,Tkinter,SQLite,Pandas',
                created_at=datetime.utcnow()
            ),
            Project(
                title='iPhone Application Design',
                description='A simple personal website based on HTML and CSS',
                image_url='static/images/projects/3.jpg',
                documentation_url='static/docs/project3.pdf',
                video_url='static/videos/3.mp4',
                github_url='https://gitlab.com/web4383802/app-design.git',
                category='UI/UX Design',
                technologies='Figma,UI Design,UX Design',
                created_at=datetime.utcnow()
            )
        ]

        for project in projects:
            db.session.add(project)
        
        db.session.commit()

if __name__ == '__main__':
    init_db()    print("Database initialized successfully!")
