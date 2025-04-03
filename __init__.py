from flask import Flask
from .config import Config

def create_app(config_class=Config):
    """Crée et configure l'instance de l'application Flask"""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Import et initialisation des services
    from .services.storage_service import StorageService
    from .services.config_generator import HAProxyConfigGenerator
    
    storage_service = StorageService()
    config_generator = HAProxyConfigGenerator(storage_service)

    # Enregistrement des blueprints
    from .routes import main_bp, backend_bp, frontend_bp, config_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(backend_bp)
    app.register_blueprint(frontend_bp)
    app.register_blueprint(config_bp)

    # Initialisation des routes
    from .routes import init_routes
    init_routes(app, storage_service, config_generator)

    return app