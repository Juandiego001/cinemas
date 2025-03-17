from apiflask import Schema, fields
from core.schemas.utils import BaseSchema


class ScheduleIn(BaseSchema):
    id = fields.Integer()
    name = fields.String()
    status = fields.String(load_default='ACTIVE')

class ScheduleOut(BaseSchema):
    id = fields.Integer()
    name = fields.String()
    status = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class SchedulesOut(Schema):
    items = fields.List(fields.Nested(ScheduleOut))
