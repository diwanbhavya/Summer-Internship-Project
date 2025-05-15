from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from models import db, User
from datetime import datetime
import os

# Create a blueprint for authentication routes
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # If user is already logged in, redirect to home
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        # Get form data
        username = request.form.get('username')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        
        # Check if user exists
        user = User.query.filter_by(username=username).first()
        
        # Check if user exists and password is correct
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.', 'danger')
            return redirect(url_for('auth.login'))
            
        # If validation passes, log in the user
        login_user(user, remember=remember)
        
        # Get the next page from the request args, or default to home
        next_page = request.args.get('next')
        if not next_page or not next_page.startswith('/'):
            next_page = url_for('main.index')
            
        flash('Login successful!', 'success')
        
        # Set a custom response to trigger the greeting
        response = redirect(next_page)
        return response
        
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    # If user is already logged in, redirect to home
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        # Get form data
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validate form data
        if not username or not email or not password or not confirm_password:
            flash('All fields are required', 'danger')
            return redirect(url_for('auth.register'))
            
        if password != confirm_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('auth.register'))
            
        # Check if username already exists
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists', 'danger')
            return redirect(url_for('auth.register'))
            
        # Check if email already exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already registered', 'danger')
            return redirect(url_for('auth.register'))
            
        # Create new user with updated model fields
        new_user = User(
            username=username,
            email=email,
            password=generate_password_hash(password, method='pbkdf2:sha256'),
            created_at=datetime.utcnow()
        )
        
        # Add user to database
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('auth.login'))
        
    return render_template('register.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))

@auth_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@auth_bp.route('/update_profile', methods=['POST'])
@login_required
def update_profile():
    """Update user profile information"""
    # Check current password
    current_password = request.form.get('current_password')
    if not check_password_hash(current_user.password, current_password):
        flash('Current password is incorrect.', 'danger')
        return redirect(url_for('auth.profile'))
    
    # Update user information
    current_user.username = request.form.get('username')
    current_user.email = request.form.get('email')
    current_user.full_name = request.form.get('full_name')
    current_user.bio = request.form.get('bio')
    current_user.updated_at = datetime.utcnow()
    
    # Handle password change if provided
    new_password = request.form.get('new_password')
    if new_password:
        current_user.password = generate_password_hash(new_password, method='pbkdf2:sha256')
    
    # Handle avatar upload if provided
    avatar_file = request.files.get('avatar')
    if avatar_file and avatar_file.filename:
        # Define allowed file extensions
        allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
        
        # Check if the file extension is allowed
        filename = secure_filename(avatar_file.filename)
        file_ext = filename.rsplit('.', 1)[1].lower() if '.' in filename else ''
        
        if file_ext in allowed_extensions:
            # Create a unique filename
            unique_filename = f"avatar_{current_user.id}_{int(datetime.now().timestamp())}.{file_ext}"
            
            # Ensure uploads directory exists
            uploads_dir = os.path.join(current_app.static_folder, 'uploads', 'avatars')
            if not os.path.exists(uploads_dir):
                os.makedirs(uploads_dir)
            
            # Save the file
            file_path = os.path.join(uploads_dir, unique_filename)
            avatar_file.save(file_path)
            
            # Update user avatar URL
            current_user.avatar = url_for('static', filename=f'uploads/avatars/{unique_filename}')
        else:
            flash('Invalid file format. Please upload a PNG, JPG, JPEG, or GIF file.', 'warning')
    
    # Save changes to database
    db.session.commit()
    
    flash('Your profile has been updated successfully!', 'success')
    return redirect(url_for('auth.profile'))