from flask import Blueprint, render_template
from flask_login import login_required

# Create a blueprint for main routes
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Route for the home page"""
    return render_template('index.html')

@main_bp.route('/about')
@login_required
def about():
    """Route for the about page"""
    return render_template('about.html')

@main_bp.route('/services')
@login_required
def services():
    """Route for the services page"""
    return render_template('services.html')

@main_bp.route('/calculator')
@login_required
def calculator():
    """Route for the calculator demo page"""
    return render_template('calculator.html')

@main_bp.route('/gallery')
@login_required
def gallery():
    """Route for the image gallery page"""
    return render_template('gallery.html')

@main_bp.route('/slideshow')
@login_required
def slideshow():
    """Route for the image slideshow page"""
    return render_template('slideshow.html')

@main_bp.route('/internship')
@login_required
def internship():
    """Route for the internship landing page"""
    return render_template('internship.html')