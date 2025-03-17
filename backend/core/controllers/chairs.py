from core.app import db
from core.models import Chair
from core.services import chairs
from apiflask import APIBlueprint, abort
from core.schemas.utils import Message, Pagination
from core.schemas.chairs import ChairIn, ChairOut, ChairsOut


bp = APIBlueprint('chairs', __name__)


@bp.get('/')
@bp.input(Pagination, location='query')
@bp.output(ChairsOut)
def get_chairs(query_data):
    '''Get chairs'''

    try:
        return {'items': chairs.get_chairs(query_data['search'], 
                                         query_data['page'],
                                         query_data['per_page'])}
    except Exception as ex:
        abort(str(ex))


@bp.get('/<int:category_id>')
@bp.output(ChairOut)
def get_category(category_id):
    '''Get user'''

    try:
        return chairs.get_user(category_id)
    except Exception as ex:
        abort(str(ex))


@bp.put('/<int:category_id>')
@bp.input(ChairIn)
@bp.output(Message)
def update_chairs(category_id, json_data):
    '''Update user'''
    try:
        chairs.update_user(category_id, json_data)
        return {'message': 'User updated successfuly'}
    except Exception as ex:
        print(str(ex))
        abort(str(ex))


@bp.delete('/<int:category_id>')
@bp.output(Message)
def delete_chairs(category_id):
    '''Delete chairs'''

    try:
        chairs.delete_user(category_id)
        return {'message': 'User deleted successfuly'}
    except Exception as ex:
        print(str(ex))
        abort(str(ex))
