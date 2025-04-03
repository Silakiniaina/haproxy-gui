from flask import Blueprint, request, redirect, url_for, render_template, jsonify
from models.backend import Backend
from models.server import Server
from services.storage_service import StorageService

backend_bp = Blueprint('backend', __name__)

@backend_bp.route('/backend/add', methods=['GET', 'POST'])
def add_backend():
    if request.method == 'POST':
        backend = Backend(
            name=request.form['name'],
            mode=request.form['mode'],
            balance=request.form['balance'],
            timeout_connect=request.form.get('timeout_connect', '5s'),
            timeout_server=request.form.get('timeout_server', '50s'),
            timeout_check=request.form.get('timeout_check', '5s'),
            check_enabled='check_enabled' in request.form,
            option_httpchk=request.form.get('option_httpchk'),
            cookie=request.form.get('cookie'),
            cookie_type=request.form.get('cookie_type', 'insert'),
            forwardfor='forwardfor' in request.form,
            option_redispatch='option_redispatch' in request.form,
            maxconn=int(request.form.get('maxconn', 2000)),
            retries=int(request.form.get('retries', 3))
        )
        storage_service.add_backend(backend)
        return redirect(url_for('main.index'))
    return render_template('backend_form.html')