from flask import Flask
from config import Config
from services.storage_service import StorageService
from services.config_generator import HAProxyConfigGenerator

# Import blueprints and init functions
from routes.main_routes import main_bp, init_routes as init_main_routes
from routes.backend_routes import backend_bp, init_routes as init_backend_routes
from routes.frontend_routes import frontend_bp, init_routes as init_frontend_routes
from routes.config_routes import config_bp, init_routes as init_config_routes

app = Flask(__name__)
app.config.from_object(Config)

# Initialize services

storage_service = StorageService()
config_generator = HAProxyConfigGenerator(storage_service)

# Set up storage for routes
init_main_routes(storage_service)
init_backend_routes(storage_service)
init_frontend_routes(storage_service)
init_config_routes(config_generator)

# Register blueprints
app.register_blueprint(main_bp)
app.register_blueprint(backend_bp)
app.register_blueprint(frontend_bp)
app.register_blueprint(config_bp)

if __name__ == '__main__':
    app.run(debug=True)


