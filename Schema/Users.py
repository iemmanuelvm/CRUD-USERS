from marshmallow import Schema, fields


class UserSchemaCreate(Schema):
    # Here are defined the field to db
    id = fields.UUID(dump_only=True, required=True)
    name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True)

class UserSchemaUpdate(Schema):
    # Here are defined the field to db
    name = fields.String()
    last_name = fields.String()
    email = fields.Email()
    phone = fields.String()