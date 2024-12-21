from flask import Flask, render_template
from routes import register_routes
from config.settings import load_config
from services.database import get_db_connection
from os.path import splitext

app = Flask(__name__)

# Load configuration
load_config(app)

# Register all routes
register_routes(app)

# Template filters
@app.template_filter('remove_extension')
def remove_extension(value):
    """Remove file extension from string"""
    return splitext(value)[0]

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=500, debug=True)