from flask_restplus import Resource, Namespace, abort
from todo.core import *
from flask import request
from .model import TODODetails, TODO

ns = Namespace('TODO', description="TODO related operations")

@ns.route('/todo')
class TodoList(Resource):
    def get(self):
        return get_todos(), 200

    def post(self):
        result, errors = self.validate_data(request.data, 'POST')

        if errors:
            abort(400, result)

        result, errors = add_todo(result)
        if errors:
            abort(400, result)
        else:
            return 'Successfully added todos.', 200

    def put(self):
        result, errors = self.validate_data(request.data, "PUT")

        if errors:
            abort(400, result)

        result, errors = update_todo(result['username'], result['todos'])
        if errors:
            abort(400, result)
        else:
            return "Successfully updated todos", 200


    def delete(self):
        result, errors = self.validate_data(request.data, 'POST')

        if errors:
            abort(400, result)

        todos_delete = [t['name'] for t in result['todos']]
        print(result['username'])
        print(todos_delete)
        result, errors = delete_todo(result['username'], todos_delete)

        if errors:
            abort(400, result)
        else:
            return 'Successfully deleted todos.', 200

    def validate_data(self, data, method):
        if not data:
            return 'Empty Data', -1
        if method == 'POST' or method == "DELETE" or method == "PUT":
            if data:
                try:
                    result = TODODetails().loads(data)
                except:
                    return 'Invalid JSON', -1

            if result.errors:
                return 'Request Data Validation failed', -1
            else:
                return result.data, 0



