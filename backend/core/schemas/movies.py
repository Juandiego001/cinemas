from apiflask import Schema, fields
from core.schemas.utils import BaseSchema


class MovieIn(BaseSchema):
    id = fields.Integer()
    name = fields.String()
    trailerVideo = fields.File()
    duration_minutes = fields.Integer(data_key='durationMinutes')
    classification_age = fields.Integer(data_key='classificationAge')
    category_id = fields.Integer(data_key='categoryId')
    status = fields.String(load_default='ACTIVE')


class MovieOut(BaseSchema):
    id = fields.Integer()
    name = fields.String()
    duration_minutes = fields.Integer(data_key='durationMinutes')
    classification_age = fields.Integer(data_key='classificationAge')
    category_id = fields.Integer(data_key='categoryId')
    status = fields.String(load_default='ACTIVE')


class MoviesOut(Schema):
    items = fields.List(fields.Nested(MovieOut))


class MovieCategoryOut(MovieOut):
    trailer_video = fields.String(data_key='trailerVideo')


class MoviesCategoryOut(Schema):
    items = fields.List(fields.Nested(MovieCategoryOut))
