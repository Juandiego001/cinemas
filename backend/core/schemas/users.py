from bcrypt import hashpw, gensalt, checkpw
from http.client import HTTPException
from core.models import User
from apiflask import Schema, fields
from marshmallow import post_load, pre_load, validates_schema
from core.app import db
from core.schemas.utils import BaseSchema


class UserInLogIn(BaseSchema):
    email = fields.String()
    password = fields.String()

    @validates_schema
    def login(self, data, **kwargs):
        '''Log In User'''

        user = db.session.query(User).filter(User.email == data['email']).first()
        if not user or not checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
            raise HTTPException('User or password incorrect')
        return user
    
    @post_load
    def make_object(self, data, **kwargs):
        print('DATA: ', data)
        return data


class UserIn(BaseSchema):
    id = fields.Integer()
    full_name = fields.String(data_key='fullName')
    email = fields.String()
    password = fields.String()
    document = fields.String()
    status = fields.String(load_default='ACTIVE')


class UserInCreate(UserIn):
    full_name = fields.String(data_key='fullName')
    email = fields.String()
    password = fields.String()
    document = fields.String()

    @pre_load
    def serialize_password(self, data, **kwargs):
        new_password = data['password'].encode('utf-8')
        new_password = hashpw(new_password, gensalt()).decode('utf-8')
        data['password'] = new_password
        data['status'] = 'ACTIVE'
        del data['id']
        return data

    @post_load
    def make_object(self, data, **kwargs):
        return User(**data)


class UserInUpdate(UserIn):

    @post_load
    def make_object(self, data, **kwargs):
        return User(**data)


class UserOut(BaseSchema):
    id = fields.Integer()
    full_name = fields.String(data_key='fullName')
    email = fields.String()
    document = fields.String()
    status = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class UsersOut(Schema):
    items = fields.List(fields.Nested(UserOut))
