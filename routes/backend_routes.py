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

@backend_bp.route('/backend/<name>/edit', methods=['GET', 'POST'])
def edit_backend(name):
    backend = storage_service.get_backend(name)
    if not backend:
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        backend.mode = request.form['mode']
        backend.balance = request.form['balance']
        backend.timeout_connect = request.form.get('timeout_connect', '5s')
        backend.timeout_server = request.form.get('timeout_server', '50s')
        backend.timeout_check = request.form.get('timeout_check', '5s')
        backend.check_enabled = 'check_enabled' in request.form
        backend.option_httpchk = request.form.get('option_httpchk')
        backend.cookie = request.form.get('cookie')
        backend.cookie_type = request.form.get('cookie_type', 'insert')
        backend.forwardfor = 'forwardfor' in request.form
        backend.option_redispatch = 'option_redispatch' in request.form
        backend.maxconn = int(request.form.get('maxconn', 2000))
        backend.retries = int(request.form.get('retries', 3))
        return redirect(url_for('main.index'))
    # Check status of all servers before rendering
    for server in backend.servers.values():
        server.check_status()
    return render_template('backend_form.html', backend=backend)

@backend_bp.route('/backend/<name>/delete')
def delete_backend(name):
    storage_service.delete_backend(name)
    return redirect(url_for('main.index'))

@backend_bp.route('/backend/<backend_name>/server/add', methods=['GET', 'POST'])
def add_server(backend_name):
    backend = storage_service.get_backend(backend_name)
    if not backend:
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        server = Server(
            name=request.form['name'],
            host=request.form['host'],
            port=int(request.form['port']),
            weight=int(request.form.get('weight', 1)),
            check='check' in request.form,
            check_port=int(request.form['check_port']) if request.form.get('check_port') else None,
            check_inter=request.form.get('check_inter', '2s'),
            check_fall=int(request.form.get('check_fall', 3)),
            check_rise=int(request.form.get('check_rise', 2)),
            maxconn=int(request.form.get('maxconn', 1000)),
            backup='backup' in request.form,
            disabled='disabled' in request.form,
            maintenance='maintenance' in request.form
        )
        server.check_status()  # Check status immediately after creation
        backend.servers[server.name] = server
        return redirect(url_for('main.index'))
    return render_template('server_form.html', backend_name=backend_name)
