from flask import Blueprint, render_template
from services.storage_service import StorageService

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # Check status of all servers before rendering
    for backend in storage_service.backends.values():
        for server in backend.servers.values():
            server.check_status()
    return render_template('index.html', 
                         frontends=storage_service.frontends, 
                         backends=storage_service.backends)
