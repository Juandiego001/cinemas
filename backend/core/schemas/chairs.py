from apiflask import Schema, fields
from core.schemas.utils import BaseSchema


class ChairIn(BaseSchema):
    id = fields.Integer()
    name = fields.String()
    status = fields.String(load_default='ACTIVE')

class ChairOut(BaseSchema):
    id = fields.Integer()
    name = fields.String()
    status = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class ChairsOut(Schema):
    items = fields.List(fields.Nested(ChairOut))
