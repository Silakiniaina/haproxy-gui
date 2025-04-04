import subprocess
from flask import Blueprint, redirect, render_template, request, url_for, flash
from services.config_generator import HAProxyConfigGenerator

config_bp = Blueprint('config', __name__)

# Global config generator variable
config_generator = None

@config_bp.route('/config')
def show_config():
    config = config_generator.generate_config()
    return render_template('config.html', config=config)

# Endpoint pour valider la configuration et recharger HAProxy
@config_bp.route('/config/validate', methods=['POST'])
def validate_config():
    try:
        config_data = request.form.get('config_data')
        haproxy_config_path = '/etc/haproxy/haproxy.cfg' 
        with open(haproxy_config_path, 'w') as config_file:
            config_file.write(config_data)

        subprocess.run(['systemctl', 'restart', 'haproxy'], check=True)

        return redirect(url_for('main.index'))  
    except Exception as e:
        return f"Erreur lors de la validation de la configuration : {str(e)}", 500

# Endpoint pour retourner vers l'index
@config_bp.route('/config/back')
def go_back():
    return redirect(url_for('main.index'))

# New endpoint to start HAProxy
@config_bp.route('/config/start', methods=['POST'])
def start_haproxy():
    try:
        subprocess.run(['systemctl', 'start', 'haproxy'], check=True)
        flash('HAProxy started successfully!', 'success')
    except Exception as e:
        flash(f"Error starting HAProxy: {str(e)}", 'error')
    return redirect(url_for('main.index'))

# New endpoint to stop HAProxy
@config_bp.route('/config/stop', methods=['POST'])
def stop_haproxy():
    try:
        subprocess.run(['systemctl', 'stop', 'haproxy'], check=True)
        flash('HAProxy stopped successfully!', 'success')
    except Exception as e:
        flash(f"Error stopping HAProxy: {str(e)}", 'error')
    return redirect(url_for('main.index'))

# Function to initialize the config generator
def init_routes(generator: HAProxyConfigGenerator):
    global config_generator
    config_generator = generator

