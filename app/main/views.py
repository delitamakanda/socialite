from datetime import datetime
from flask import render_template, session, redirect, url_for, request
from . import main
from .forms import NameForm
from .. import db
from ..models import User

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
