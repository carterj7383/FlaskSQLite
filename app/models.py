from . import db

class User(db.Model):
    __tablename__ = 'users'
    email = db.Column(db.String(120), primary_key=True)
    password = db.Column(db.String(120), nullable=False)
    
    def __repr__(self):
        return f'<User {self.email}>'


from flask import Blueprint, request, render_template
from .models import User

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        user = User.query.filter_by(
            email=request.form['email'],
            password=request.form['password']
        ).first()
        if user:
            message = "Login successful!"
        else:
            message = "Invalid credentials"
    return render_template('login.html', message=message)