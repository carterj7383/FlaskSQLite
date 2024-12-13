from flask import Blueprint, request, render_template
from .models import User
from . import db


main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def login():
    """Handle login page requests"""
    message = None
    
    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')
        

        user = User.query.filter_by(
            email=email,
            password=password  
        ).first()
        

        if user:
            message = "Login successful!"
        else:
            message = "Invalid credentials"
            
    return render_template('login.html', message=message)


@main.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration"""
    message = None
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            message = "Email already registered"
        else:

            new_user = User(email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            message = "Registration successful!"
            
    return render_template('register.html', message=message)