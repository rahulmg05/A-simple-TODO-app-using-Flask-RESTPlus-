from flask_restplus import Api
from .todo import api as todo_api

api = Api(title="Resource-TODO", version='0.1', description="TODO related API's", doc=False)

api.add_namespace(todo_api, path="/api/v0.1")