from flask import Blueprint, request, redirect, url_for, render_template
from models.frontend import Frontend
from services.storage_service import StorageService

frontend_bp = Blueprint('frontend', __name__)