from functools import wraps
from apiflask.exceptions import abort
from flask.globals import request
from flask_jwt_extended.utils import get_jwt
from core.models import Permission, Module, Group, UserGroup, User
from flask_sqlalchemy.query import Query
from core.app import db
from sqlalchemy import case, or_


def get_user_permissions(user_id: str) -> dict:
    def get_query_permission(action: str) -> Query:
        permission_column = getattr(Permission, action)
        return db.session.query(
            Module.name.label('slug'),
            case((permission_column, action)).label('action')
        )\
            .join(Permission, Permission.module_id == Module.id)\
            .join(Group, Group.id == Permission.group_id)\
            .join(UserGroup, UserGroup.group_id == Group.id)\
            .join(User, User.id == UserGroup.user_id)\
            .filter(User.id == user_id, permission_column)

    query_read = get_query_permission('read')
    query_update = get_query_permission('update')
    query_create = get_query_permission('create')
    query_delete = get_query_permission('delete')
    query = query_read.union(query_update)\
        .union(query_create)\
        .union(query_delete)
    return query.all()


def get_permission(email: str, name: str, actions: list[str]) -> bool:
    permission_columns = [getattr(Permission, action) for action in actions]
    return db.session.scalars(db.select(Module)
                              .join(Permission)
                              .join(Group)
                              .join(UserGroup)
                              .join(User)
                              .where(User.email == email,
                                     Module.name == name,
                                     or_(*permission_columns),
                                     Group.status)).first()


def permissions_required(module):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            if get_jwt():
                email = get_jwt()['email']
                action_methods = {'GET': ['read'],
                                  'POST': ['create'],
                                  'PATCH': ['update'],
                                  'DELETE': ['delete'],
                                  'PUT': ['create', 'update']}
                actions = action_methods[request.method]
                if not get_permission(email, module, actions):
                    abort(400, 'Permisos insuficientes')
            return fn(*args, **kwargs)
        return decorator
    return wrapper


def type_jwt_required(jwt_type: list):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            if get_jwt():
                if get_jwt()['type_jwt'] not in jwt_type:
                    abort(400, 'Permisos insuficientes')
            return fn(*args, **kwargs)
        return decorator
    return wrapper
