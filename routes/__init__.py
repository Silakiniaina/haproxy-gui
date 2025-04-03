from .main_routes import main_bp, init_routes as init_main_routes
from .backend_routes import backend_bp, init_routes as init_backend_routes
from .frontend_routes import frontend_bp, init_routes as init_frontend_routes
from .config_routes import config_bp, init_routes as init_config_routes

def init_all_routes(storage_service, config_generator):
    """Initialize routes with required services."""
    init_main_routes(storage_service)
    init_backend_routes(storage_service)
    init_frontend_routes(storage_service)
    init_config_routes(config_generator)
