from apiflask import fields, Schema
from marshmallow import EXCLUDE


class BaseSchema(Schema):
    class Meta:
        unknown = EXCLUDE


class Pagination(Schema):
    search = fields.String()
    page = fields.Integer()
    per_page = fields.Integer(data_key='perPage')


class Message(Schema):
    message = fields.String()
