from flask import Blueprint, jsonify, request
from models import Comment
from extensions import db
from datetime import datetime

api = Blueprint('api', __name__)

@api.route('/projects/<int:project_id>/comments', methods=['POST'])
def add_comment(project_id):
    data = request.get_json()
    
    comment = Comment(
        content=data.get('content'),
        author=data.get('author'),
        project_id=project_id,
        created_at=datetime.utcnow()
    )
    
    db.session.add(comment)
    db.session.commit()
    
    return jsonify({
        'success': True,
        'comment': {
            'id': comment.id,
            'content': comment.content,
            'author': comment.author,
            'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M')
        }
    }) 