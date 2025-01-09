from flask import Blueprint, render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from models import User, Comment, Project
from extensions import db
from forms import LoginForm, RegisterForm

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash('登录成功！', 'success')
            next_page = request.args.get('next')
            return redirect(next_page if next_page else url_for('main.index'))
        flash('邮箱或密码错误！', 'error')
    return render_template('auth/login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash('该邮箱已被注册！', 'error')
            return redirect(url_for('auth.register'))
        
        user = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=generate_password_hash(form.password.data)
        )
        
        db.session.add(user)
        db.session.commit()
        
        flash('注册成功！请登录。', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已成功登出！', 'success')
    return redirect(url_for('main.index'))

@auth.route('/profile')
@login_required
def profile():
    user_comments = Comment.query.filter_by(author=current_user.username)\
                               .order_by(Comment.created_at.desc())\
                               .all()
    comments_with_projects = []
    for comment in user_comments:
        project = Project.query.get(comment.project_id)
        comments_with_projects.append({
            'comment': comment,
            'project': project
        })
    
    return render_template('auth/profile.html', 
                         user=current_user, 
                         comments=user_comments,
                         comments_with_projects=comments_with_projects) 