from flask import Blueprint
from flask_restplus import Api

from .tokens import tokens
from .users import users

api_blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(api_blueprint, version="v1", doc='/docs')
api.add_namespace(users, '/')
api.add_namespace(tokens, '/token')
