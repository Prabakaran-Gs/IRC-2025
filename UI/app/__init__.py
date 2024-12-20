from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configuration setup (e.g., SECRET_KEY, database URIs)
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Import routes
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
