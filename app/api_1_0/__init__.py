from flask import Blueprint

api = Blueprint('api', __name__)

from . import authentication, post, comment, user, errors
