from flask import Blueprint

notebook_blueprint = Blueprint('notebook_bp', __name__, template_folder="templates/enterprises")

from . import views