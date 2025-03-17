from core.app import db
from core.models import Chair
from sqlalchemy import or_, and_
from werkzeug.exceptions import HTTPException


def get_chairs(search: str, page: int, per_page: int):
    '''Get chairs'''

    query = Chair.status == 'ACTIVE'
    if search:
        query = and_(Chair.status == 'ACTIVE',
                     or_(Chair.name.ilike(f'%{search}%')))

    return db.paginate(db.session.query(Chair).filter(query),
                       page=page, per_page=per_page)


def get_chair(chair_id: int):
    '''Get chair by chair id'''

    return db.session.query(Chair).filter(Chair.id == chair_id).first()


def check_chair_exists(chair_id: int):
    '''Check if chair exists'''

    return db.session.query(Chair).filter(Chair.id == chair_id).first()


def update_chair(chair_id: int, chair_load):
    '''Update chair'''

    if not check_chair_exists(chair_id):
        raise HTTPException('Chair not found')

    db.session.merge(chair_load)
    db.session.commit()


def delete_chair(chair_id: int):
    '''Delete chair'''

    db.session.merge(Chair(id=chair_id, status='INACTIVE'))
    db.session.commit()
