from marshmallow import Schema, fields, validates, ValidationError

class TODO(Schema):
    name = fields.String(
        required=True,
        error_messages={"required":"'name' is a required field"},
    )
    description = fields.String(
        required=True,
        error_messages={"required": "'description' is a required field"}
    )


class TODODetails(Schema):
    username = fields.String(
        required=True,
        error_messages={"required": "'username' is a required field"}
    )
    date_created = fields.DateTime()
    date_modified = fields.DateTime()
    todos = fields.List(
        fields.Nested(TODO),
        required=True,
        error_messages={"required": "'todos' is a required field"}
    )

    @validates('todos')
    def validate_todos(self, value):
        if not value:
            raise ValidationError("The todos field cannot have an empty list")

