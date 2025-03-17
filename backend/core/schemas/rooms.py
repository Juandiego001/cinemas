from apiflask import Schema, fields
from core.schemas.utils import BaseSchema


class RoomIn(BaseSchema):
    id = fields.Integer()
    name = fields.String()
    status = fields.String(load_default='ACTIVE')


class RoomOut(BaseSchema):
    id = fields.Integer()
    name = fields.String()
    status = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class RoomsOut(Schema):
    items = fields.List(fields.Nested(RoomOut))
