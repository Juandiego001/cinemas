from core.app import db
from core.models import Room
from core.services import rooms
from apiflask import APIBlueprint, abort
from core.schemas.utils import Message, Pagination
from core.schemas.rooms import RoomIn, RoomOut, RoomsOut


bp = APIBlueprint('rooms', __name__)


@bp.get('/')
@bp.input(Pagination, location='query')
@bp.output(RoomsOut)
def get_rooms(query_data):
    '''Get rooms'''

    try:
        return {'items': rooms.get_rooms(query_data['search'], 
                                         query_data['page'],
                                         query_data['per_page'])}
    except Exception as ex:
        abort(str(ex))


@bp.get('/<int:room_id>')
@bp.output(RoomOut)
def get_room(room_id):
    '''Get room'''

    try:
        return rooms.get_room(room_id)
    except Exception as ex:
        abort(str(ex))


@bp.put('/<int:room_id>')
@bp.input(RoomIn)
@bp.output(Message)
def update_rooms(room_id, json_data):
    '''Update room'''
    try:
        rooms.update_room(room_id, json_data)
        return {'message': 'room updated successfuly'}
    except Exception as ex:
        print(str(ex))
        abort(str(ex))


@bp.delete('/<int:room_id>')
@bp.output(Message)
def delete_rooms(room_id):
    '''Delete rooms'''

    try:
        rooms.delete_room(room_id)
        return {'message': 'room deleted successfuly'}
    except Exception as ex:
        print(str(ex))
        abort(str(ex))
