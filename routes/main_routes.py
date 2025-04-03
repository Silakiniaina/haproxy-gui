from flask import Blueprint, render_template
from services.storage_service import StorageService

main_bp = Blueprint('main', __name__)
