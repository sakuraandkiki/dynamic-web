"""Main route handlers."""
from flask import Blueprint, render_template, abort, jsonify, request, send_file, flash, redirect, url_for
from flask_login import current_user, login_required
from models import Project, Comment, Contact
from extensions import db
from forms import CommentForm, ContactForm
from datetime import datetime
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    projects = Project.query.all()
    return render_template('main/index.html', projects=projects)

@main.route('/project/<int:project_id>')
def show_project(project_id):
    project = Project.query.get_or_404(project_id)
    form = CommentForm()
    return render_template('main/show_project.html', project=project, form=form)

@main.route('/api/projects/<int:project_id>/comments', methods=['POST'])
@login_required
def add_comment(project_id):
    project = Project.query.get_or_404(project_id)
    form = CommentForm()
    
    if form.validate_on_submit():
        comment = Comment(
            content=form.content.data,
            author=current_user.username,
            project_id=project_id,
            created_at=datetime.utcnow()
        )
        
        db.session.add(comment)
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'comment': {
                'id': comment.id,
                'content': comment.content,
                'author': comment.author,
                'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M')
            }
        })
    
    return jsonify({
        'status': 'error',
        'errors': form.errors
    }), 400

@main.route('/download/<int:project_id>')
def download_file(project_id):
    project = Project.query.get_or_404(project_id)
    file_path = os.path.join('static', 'files', f'{project_id}.zip')
    try:
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        flash('文件下载失败！', 'error')
        return redirect(url_for('main.show_project', project_id=project_id))

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(
            name=form.name.data,
            email=form.email.data,
            subject=form.subject.data,
            message=form.message.data
        )
        db.session.add(contact)
        db.session.commit()
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('main.contact'))
    return render_template('main/contact.html', form=form)