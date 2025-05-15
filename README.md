# Summer-Internship-Project
# Flask Web Application

A complete web application built with Flask framework offering various features including authentication, calculator, gallery, and more.

## Project Overview

This Flask application provides multiple features like user authentication (register/login), profile management, calculator, gallery, and informational pages such as about, services, internship, and contact.

## Project Structure

```
bhavya/
├── .venv/                  # Python virtual environment
├── instance/               # Flask instance folder (contains site.db)
├── routes/                 # Route blueprints
│   ├── __init__.py
│   ├── auth_routes.py      # Authentication routes (login, register)
│   ├── form_handler.py     # Form processing routes
│   └── main_routes.py      # Main website routes
├── static/                 # Static assets
│   ├── css/                # Stylesheets
│   ├── images/             # Image files
│   └── js/                 # JavaScript files
├── templates/              # HTML templates
│   ├── about.html
│   ├── base.html           # Base template others extend from
│   ├── calculator.html
│   ├── contact.html
│   ├── gallery.html
│   ├── index.html          # Homepage
│   ├── internship.html
│   ├── login.html
│   ├── profile.html
│   ├── register.html
│   ├── services.html
│   ├── slideshow.html
│   └── tp.html
├── app.py                  # Main application entry point
├── config.py               # Configuration settings
├── models.py               # Database models
└── requirements.txt        # Package dependencies
```

### Core Features
- **User Authentication**: Register, login, and secure session management
- **Profile Management**: User profile customization and management
- **Interactive Calculator**: Client-side calculator with API integration
- **Image Gallery**: Responsive gallery with image modal view
- **Slideshow Component**: Dynamic image slideshow with automatic transitions
- **Form Handling**: Contact form and other data submission capabilities
- **Responsive Design**: Mobile-friendly interface with menu toggle

### Advanced Features
- **Time-based Greetings**: Dynamic welcome messages based on time of day
- **Custom Alert System**: Enhanced user notifications
- **API Integration**: Backend API for calculator operations
- **Interactive UI Elements**: Color changing buttons and dynamic components
- **Session Management**: Secure user session handling

## Technology Stack

### Backend
- **Flask**: Web framework for Python
- **SQLAlchemy**: ORM for database operations
- **Flask-Login**: Authentication management
- **Flask-Bcrypt**: Password hashing and security
- **Werkzeug**: WSGI web application library

### Frontend
- **HTML5/CSS3**: Structure and styling
- **JavaScript**: Client-side interactivity
- **Jinja2**: Templating engine
- **Responsive Design**: Mobile-friendly approach

### Database
- **SQLite**: Development database (easily configurable for PostgreSQL/MySQL in production)

## Installation & Setup

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/cognifyz-webapp.git
   cd cognifyz-webapp
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   
   # Activate the environment
   # On Windows:
   .venv\Scripts\activate
   
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the application**:
   - Review and update `config.py` as needed
   - Set up any environment variables required

5. **Initialize the database**:
   ```bash
   # Start Python interpreter
   python
   
   # In Python console:
   from app import app, db
   with app.app_context():
       db.create_all()
   exit()
   ```

6. **Run the application**:
   ```bash
   python app.py
   ```

7. **Access the application**:
   Open your browser and navigate to `http://127.0.0.1:5000/`

## Pages & Functionality

### Home Page (`index.html`)
- Welcome section
- CTA buttons for login/register
- Introduction to internship opportunities

### Authentication Pages
- **Register** (`register.html`): User registration form
- **Login** (`login.html`): Authentication form
- **Profile** (`profile.html`): User profile management

### Core Content Pages
- **About** (`about.html`): Company information
- **Services** (`services.html`): Services offered
- **Internship** (`internship.html`): Internship program details
- **Contact** (`contact.html`): Contact form and information

### Interactive Features
- **Calculator** (`calculator.html`): Interactive calculator with API backend
- **Gallery** (`gallery.html`): Image gallery with modal view
- **Slideshow** (`slideshow.html`): Dynamic image slideshow component

## Authentication System

The authentication system uses Flask-Login and Flask-Bcrypt to provide secure user registration and login functionality:

- Password hashing for secure storage
- Session-based authentication
- User role management
- Protected routes requiring authentication
- Remember-me functionality

## Interactive Features

### JavaScript Functionalities
- **Time-based Greetings**: Shows different welcome messages based on time of day
- **Custom Alert System**: Enhanced user notifications
- **Color-changing Elements**: Interactive UI components
- **Calculator API Integration**: Performs calculations via backend API
- **Modal Image Viewer**: Enlarges gallery images
- **Responsive Menu Toggle**: Enhanced mobile experience
- **Automatic Slideshow**: Image rotation with timing controls

## API Endpoints

### Calculator API
- **Endpoint**: `/api/calculate`
- **Method**: POST
- **Parameters**:
  - `num1`: First number
  - `num2`: Second number
  - `operation`: Mathematical operation (add, subtract, multiply, divide)
- **Response**: JSON with calculation result

## Screenshots

Demonstrating the project:

### Home Page
![Home Page](![image](https://github.com/user-attachments/assets/3c6c660d-56b4-4d3b-82e9-a0211c6b675d)
)

### Login Screen
![Login Screen](![image](https://github.com/user-attachments/assets/e4bec438-6c23-4369-9048-6fed22c23aec)
)

### User Profile
![User Profile](![image](https://github.com/user-attachments/assets/b55f4bd0-0920-421b-b514-b838f3991549)
)

### Calculator Interface
![Calculator](![image](https://github.com/user-attachments/assets/5f326606-49b1-4145-8dbc-b2b539cf8658)
)

### Image Gallery
![Gallery](![image](https://github.com/user-attachments/assets/911e7bd6-8c58-4b3f-928e-4edd61fd118f)
)

### Slideshow Component
![Slideshow](![image](https://github.com/user-attachments/assets/eadf4847-daa7-4e2a-a642-523a974ca32a)
)

### Contact Form
![Contact Form](![image](https://github.com/user-attachments/assets/f3fc715e-a487-40ee-98de-e0b112a0ddb5)
)


### Development Workflow
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

### Coding Standards
- Follow PEP 8 guidelines for Python code
- Use clear, descriptive variable and function names
- Comment complex sections of code
- Write unit tests for new features

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

© 2023 Cognifyz Technologies. All Rights Reserved.
