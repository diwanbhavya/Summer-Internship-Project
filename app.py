from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

from routes.main_routes import main_bp
from routes.form_handler import form_bp
from routes.auth_routes import auth_bp
from models import db, User

app = Flask(__name__)

# Configuration
app.config.from_object('config')

# Initialize database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register blueprints
app.register_blueprint(main_bp)
app.register_blueprint(form_bp)
app.register_blueprint(auth_bp)

# Create database tables
with app.app_context():
    db.create_all()
    # Create an admin user if no users exist
    if not User.query.first():
        admin = User(
            username='admin',
            email='admin@example.com',
            password=generate_password_hash('admin123', method='pbkdf2:sha256')
        )
        db.session.add(admin)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)