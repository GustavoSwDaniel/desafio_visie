from flask import Blueprint

bp = Blueprint('people', __name__)

from visie.people import controller
