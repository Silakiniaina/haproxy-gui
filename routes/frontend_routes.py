from flask import Blueprint, request, redirect, url_for, render_template
from models.frontend import Frontend
from services.storage_service import StorageService

frontend_bp = Blueprint('frontend', __name__)

@frontend_bp.route('/frontend/add', methods=['GET', 'POST'])
def add_frontend():
    if request.method == 'POST':
        frontend = Frontend(
            name=request.form['name'],
            bind=request.form['bind'],
            mode=request.form['mode'],
            maxconn=int(request.form.get('maxconn', 10000)),
            timeout_client=request.form.get('timeout_client', '50s'),
            client_fin_timeout=request.form.get('client_fin_timeout', '1s'),
            ssl='ssl' in request.form,
            ssl_certificate=request.form.get('ssl_certificate'),
            ssl_ciphers=request.form.get('ssl_ciphers'),
            backends=request.form.getlist('backends')
        )
        storage_service.add_frontend(frontend)
        return redirect(url_for('main.index'))
    return render_template('frontend_form.html', backends=storage_service.backends)    