from app import app
import init_db

# 初始化数据库
init_db.init_db()

if __name__ == "__main__":
    app.run() 