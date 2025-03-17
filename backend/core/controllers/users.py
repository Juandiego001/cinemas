from core.app import db
from core.models import User
from core.services import users
from apiflask import APIBlueprint, abort
from core.schemas.utils import Message, Pagination
from core.schemas.users import UserInLogIn, UserInUpdate, UserInCreate, UserOut, UsersOut


bp = APIBlueprint('users', __name__)


@bp.get('/')
@bp.input(Pagination, location='query')
@bp.output(UsersOut)
def get_users(query_data):
    '''Get users'''

    try:
        return {'items': users.get_users(query_data['search'], 
                                         query_data['page'],
                                         query_data['per_page'])}
    except Exception as ex:
        abort(str(ex))


@bp.get('/<int:user_id>')
@bp.output(UserOut)
def get_user(user_id):
    '''Get user'''

    try:
        return users.get_user(user_id)
    except Exception as ex:
        abort(str(ex))


@bp.post('/login')
@bp.input(UserInLogIn, arg_name='user')
def login_users(user):
    '''Users Log In'''

    try:
        return {'message': 'Login succesfull', 'status': 200}
    except Exception as ex:
        print(str(ex))
        abort(str(ex))


@bp.post('/signup')
@bp.input(UserInCreate, arg_name='user')
def signup_users(user):
    '''Users Sign Up'''

    try:
        db.session.add(user)
        db.session.commit()
        return {'message': 'User registered successfully'}
    except Exception as ex:
        print(str(ex))
        abort(str(ex))


@bp.put('/<int:user_id>')
@bp.input(UserInUpdate)
@bp.output(Message)
def update_users(user_id, json_data):
    '''Update user'''
    try:
        users.update_user(user_id, json_data)
        return {'message': 'User updated successfuly'}
    except Exception as ex:
        print(str(ex))
        abort(str(ex))


@bp.delete('/<int:user_id>')
@bp.output(Message)
def delete_users(user_id):
    '''Delete users'''

    try:
        users.delete_user(user_id)
        return {'message': 'User deleted successfuly'}
    except Exception as ex:
        print(str(ex))
        abort(str(ex))
