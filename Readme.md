
## Tech Stack

### Backend
- Python 3.8+
- Flask (Web framework)
- SQLAlchemy (ORM)
- Flask-Login (User session management)
- Flask-WTF (Form handling and validation)
- Werkzeug (Password hashing)
- SQLite (Database)

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap 5
- jQuery

## API Endpoints

### Authentication
- `GET/POST /auth/login` - User login
- `GET/POST /auth/register` - User registration
- `GET /auth/logout` - User logout
- `GET /auth/profile` - User profile

### Projects
- `GET /` - Project list
- `GET /project/<id>` - Project details
- `GET /download/<id>` - File download

### Comments
- `POST /api/projects/<id>/comments` - Add comment

### Contact
- `GET/POST /contact` - Contact form

## Database Models

### User
- id (Integer, Primary Key)
- username (String, Unique)
- email (String, Unique)
- password_hash (String)
- created_at (DateTime)

### Project
- id (Integer, Primary Key)
- title (String)
- description (Text)
- image_url (String)
- documentation_url (String)
- video_url (String)
- github_url (String)
- category (String)
- technologies (String)
- created_at (DateTime)

### Comment
- id (Integer, Primary Key)
- content (Text)
- author (String)
- project_id (Integer, Foreign Key)
- created_at (DateTime)

### Contact
- id (Integer, Primary Key)
- name (String)
- email (String)
- subject (String)
- message (Text)
- created_at (DateTime)

## Author

- Name: Jiapeng Shi
- Student ID: 2110090402
- Course: Web Development
- University: SDUST

## License

This project is licensed under the MIT License.