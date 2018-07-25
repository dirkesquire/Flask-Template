from flask import Blueprint

app = Blueprint('myblueprint', __name__, template_folder='templates', static_folder='static')

from .security import auth
from . import web
from . import api