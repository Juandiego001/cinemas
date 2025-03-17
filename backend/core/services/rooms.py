from core.app import db
from core.models import Room
from sqlalchemy import or_, and_
from werkzeug.exceptions import HTTPException


def get_rooms(search: str, page: int, per_page: int):
    '''Get rooms'''

    query = Room.status == 'ACTIVE'
    if search:
        query = and_(Room.status == 'ACTIVE',
                     or_(Room.name.ilike(f'%{search}%')))

    return db.paginate(db.session.query(Room).filter(query),
                       page=page, per_page=per_page)


def get_room(room_id: int):
    '''Get room by room id'''

    return db.session.query(Room).filter(Room.id == room_id).first()


def check_room_exists(room_id: int):
    '''Check if room exists'''

    return db.session.query(Room).filter(Room.id == room_id).first()


def update_room(room_id: int, room_load):
    '''Update room'''

    if not check_room_exists(room_id):
        raise HTTPException('Room not found')

    db.session.merge(room_load)
    db.session.commit()


def delete_room(room_id: int):
    '''Delete room'''

    db.session.merge(Room(id=room_id, status='INACTIVE'))
    db.session.commit()
