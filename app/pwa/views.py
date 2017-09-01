from flask import render_template, url_for
from . import pwa

@pwa.route('/')
def pwa():
    return render_template('pwa/index.html')
