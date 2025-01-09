"""Project route handlers."""
from flask import Blueprint, render_template, request, redirect, url_for
from models import Project, Comment
from extensions import db

projects = Blueprint('projects', __name__)

@projects.route('/')
def list():
    projects = Project.query.all()
    return render_template('projects/list.html', projects=projects)

@projects.route('/<int:id>')
def show(id):
    project = Project.query.get_or_404(id)
    return render_template('projects/show.html', project=project)

@projects.route('/<int:id>/comment', methods=['POST'])
def add_comment(id):
    project = Project.query.get_or_404(id)
    content = request.form.get('content')
    author = request.form.get('author')
    
    if content and author:
        comment = Comment(
            content=content,
            author=author,
            project_id=project.id
        )
        db.session.add(comment)
        db.session.commit()
    
    return redirect(url_for('projects.show', id=id))