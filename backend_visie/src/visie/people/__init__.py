from flask import Blueprint

bp = Blueprint('people', __name__)

from src.visie.people import controller
