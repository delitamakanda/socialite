from datetime import datetime
from flask import render_template, session, redirect, url_for, request
from flask.ext.login import login_user, logout_user, login_required, current_user
from . import main
from .forms import NameForm
from .. import db
from ..models import User, Role, Permission
from ..decorators import admin_required, permission_required

@main.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), know=session.get('know', False), current_time=datetime.utcnow())


@main.route('/user/<name>')
def user(name):
    return 'hello %s' % name


@main.route('/admin')
@login_required
@admin_required
def for_admin_only():
    return "for admins!"

@main.route('/moderator')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def for_moderators_only():
    return "for moderators !"
