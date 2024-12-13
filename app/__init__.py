from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, static_url_path='', static_folder='static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your-secret-key-here'
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()  # Add this line
        # Add default admin user if it doesn't exist
        from .models import User
        if not User.query.filter_by(email='admin@example.com').first():
            admin = User(email='admin@example.com', password='admin123')
            db.session.add(admin)
            db.session.commit()
    
    from .login import main
    app.register_blueprint(main)
    
    return app