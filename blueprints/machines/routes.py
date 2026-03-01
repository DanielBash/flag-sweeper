""" - Main machine routes
 -- Docker terminal creation"""


# -- importing modules
import datetime
from flask import current_app, flash, g, abort
from flask import Blueprint, render_template, redirect, url_for
from core.flask_shortcuts.decorators import login_required, required_permissions
from core.core import create_user_container
import settings
from .forms import MachineForm
from . import socketio_routes

bp = Blueprint('machine', __name__)


@bp.route('/all', methods=['GET', 'POST'])
@login_required
@required_permissions('CREATE_CONTAINERS')
def machines():
    form = MachineForm()
    containers = settings.CONTAINERS.get(g.user.id, [])
    
    if form.validate_on_submit():
        if len(containers) >= g.user.get_permission('MAX_CONTAINERS'):
            flash('You cant create more machines.', 'Warning')
            return redirect(url_for('machine.machines'))
        
        create_user_container(user_id=g.user.id, image=form.data['distro'],
                              mem=g.user.get_permission('MAX_CONTAINER_SIZE_MB'),
                              cpu=1_000_000_000 * 0.3, pids=g.user.get_permission('MAX_CONTAINER_PROCESSES'))
        
        flash('Container created successfully.', 'Message')
        
        return redirect(url_for('machine.machines'))
    
    return render_template('machines.html', title='FS: Machines', form=form, containers=containers)

@bp.route('/<string:name>', methods=['GET'])
@login_required
def machine(name):
    containers = settings.CLIENT.containers.list(
        all=True,
        filters={
            "name": name,
            "label": [
                f"user_id={g.user.id}",
                "managed=true"
            ]
        }
    )
    
    if not containers:
        abort(404)
    
    container = containers[0]
    container.reload()
    
    return render_template('machine.html', title='FS: Machine', container=container)