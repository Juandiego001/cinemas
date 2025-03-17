from apiflask import Schema, fields
from core.schemas.utils import BaseSchema


class TicketIn(BaseSchema):
    id = fields.Integer()
    name = fields.String()
    status = fields.String(load_default='ACTIVE')


class TicketOut(BaseSchema):
    id = fields.Integer()
    name = fields.String()
    status = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class TicketsOut(Schema):
    items = fields.List(fields.Nested(TicketOut))
