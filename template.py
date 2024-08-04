import os

# Project structure
directories = [
    'Jarvis',
    'Jarvis/app',
    'Jarvis/templates',
    'Jarvis/static/css'
]

files = {
    'Jarvis/app/__init__.py': '''from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():
        # Import routes
        from . import routes

        return app
''',

    'Jarvis/app/routes.py': '''from flask import render_template, request
from app import create_app

app = create_app()

@app.route('/')
def home():
    return render_template('index.html')
''',

    'Jarvis/app/config.py': '''import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = os.getenv('DEBUG', True)
''',

    'Jarvis/templates/index.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Project</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>
<body>
    <h1>Welcome to the Flask Project</h1>
</body>
</html>
''',

    'Jarvis/static/css/styles.css': '''body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    text-align: center;
}
''',

    'Jarvis/.env': '''SECRET_KEY=your_secret_key
DEBUG=True
''',

    'Jarvis/run.py': '''from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
''',

    'Jarvis/requirements.txt': '''Flask
python-dotenv
'''
}

# Create directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)
    print(f'Created directory: {directory}')

# Create files
for filepath, content in files.items():
    with open(filepath, 'w') as file:
        file.write(content)
    print(f'Created file: {filepath}')

print('Flask project structure has been set up successfully.')
