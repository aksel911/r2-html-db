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

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html', error=error), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html', error=error), 500

@app.errorhandler(400)
def bad_request_error(error):
    return render_template('errors/400.html', error=error), 400

@app.errorhandler(403)
def forbidden_error(error):
    return render_template('errors/403.html', error=error), 403

@app.errorhandler(405)
def method_not_allowed(error):
    return render_template('errors/405.html', error=error), 405

@app.route('/')
def home():
    return render_template('home.html')

# Выведем отладочную информацию при импорте
# from routes.monster_routes import bp as monster_bp
# print("Monster blueprint loaded:", monster_bp.name, monster_bp.url_prefix)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config['PORT'], debug=True)
    
