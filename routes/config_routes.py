import subprocess
from flask import Blueprint, redirect, render_template, request, url_for
from services.config_generator import HAProxyConfigGenerator

config_bp = Blueprint('config', __name__)

# Global config generator variable
config_generator = None

@config_bp.route('/config')
def show_config():
    config = config_generator.generate_config()
    return render_template('config.html', config=config)
