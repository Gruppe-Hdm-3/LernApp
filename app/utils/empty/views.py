from typing import Dict
from flask_restx import Resource
from app.configs.base import api
# from .marshalling import profile_marshalling
# from .manager import DummyManager
# from .mapper import ProfileMapper


namespace = api.namespace(
    "/your_api",
    description="Namespace for dummy APIs."
)


@namespace.route("/")
class YourAPI(Resource):
    """Basic API for dummy."""

    pass
