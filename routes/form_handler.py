from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required

form_bp = Blueprint('forms', __name__)

@form_bp.route('/contact', methods=['GET', 'POST'])
@login_required
def contact():
    """Handle contact form submissions"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Here you would typically process the form data
        # For example, send an email, save to database, etc.

        flash('Message sent successfully!', 'success')
        return redirect(url_for('forms.contact'))
        
    return render_template('contact.html')

@form_bp.route('/api/calculate', methods=['POST'])
@login_required
def calculate():
    """API endpoint for calculator operations"""
    data = request.get_json()
    
    if not data:
        return jsonify({'success': False, 'message': 'No data provided'}), 400
    
    try:
        num1 = float(data.get('num1', 0))
        num2 = float(data.get('num2', 0))
        operation = data.get('operation', 'add')
        
        result = 0
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({'success': False, 'message': 'Cannot divide by zero'}), 400
            result = num1 / num2
        else:
            return jsonify({'success': False, 'message': 'Invalid operation'}), 400
            
        return jsonify({'success': True, 'result': result})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500