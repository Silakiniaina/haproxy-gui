import subprocess
from flask import Blueprint, redirect, render_template, request, url_for
from services.config_generator import HAProxyConfigGenerator

config_bp = Blueprint('config', __name__)

# Global config generator variable
config_generator = None
