 from app import app
import os

if __name__ == "__main__":
    # 确保数据库和表已创建
    with app.app_context():
        from extensions import db
        db.create_all()
    
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port
