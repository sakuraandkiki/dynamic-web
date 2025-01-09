document.addEventListener('DOMContentLoaded', function() {
    const commentForm = document.getElementById('comment-form');
    
    if (commentForm) {
        commentForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            // 清除之前的错误信息
            clearErrors();
            
            const projectId = commentForm.dataset.projectId;
            const formData = new FormData(commentForm);
            
            try {
                const response = await fetch(`/api/projects/${projectId}/comments`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': formData.get('csrf_token')
                    },
                    body: formData
                });
                
                const data = await response.json();
                
                if (data.status === 'success') {
                    // 添加新评论
                    addNewComment(data.comment);
                    // 清空表单
                    commentForm.reset();
                } else {
                    // 显示错误信息
                    showErrors(data.errors);
                }
            } catch (error) {
                console.error('Error:', error);
            }
        });
    }
});

function clearErrors() {
    document.querySelectorAll('.error-message').forEach(el => {
        el.textContent = '';
    });
}

function showErrors(errors) {
    for (const field in errors) {
        const errorElement = document.getElementById(`${field}-error`);
        if (errorElement) {
            errorElement.textContent = errors[field][0];
        }
    }
}

function addNewComment(comment) {
    const commentsList = document.querySelector('.comments-list');
    const newComment = document.createElement('div');
    newComment.className = 'comment';
    newComment.innerHTML = `
        <div class="comment-header">
            <span class="comment-author">${comment.author}</span>
            <span class="comment-date">${comment.created_at}</span>
        </div>
        <div class="comment-content">
            ${comment.content}
        </div>
    `;
    
    commentsList.insertBefore(newComment, commentsList.firstChild);
} 