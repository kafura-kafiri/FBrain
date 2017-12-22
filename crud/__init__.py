from flask import Blueprint


user = Blueprint('user', __name__, url_prefix='/users')
csv = Blueprint('csv', __name__, url_prefix='/csvs')