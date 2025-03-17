from core.app import db
from core.models import User
from sqlalchemy import or_, and_
from werkzeug.exceptions import HTTPException


def get_users(search: str, page: int, per_page: int):
    '''Get users'''

    query = User.status == 'ACTIVE'
    if search:
        query = and_(User.status == 'ACTIVE',
                     or_(User.full_name.ilike(f'%{search}%'),
                         User.document.ilike(f'%{search}%'),
                         User.email.ilike(f'%{search}%')))

    return db.paginate(db.session.query(User).filter(query),
                       page=page, per_page=per_page)

def get_user(user_id: int):
    '''Get user by user id'''

    return db.session.query(User).filter(User.id == user_id).first()


def check_user_exists(user_id: int):
    '''Check if user exists'''

    return db.session.query(User).filter(User.id == user_id).first()


def update_user(user_id: int, user_load):
    '''Update user'''

    if not check_user_exists(user_id):
        raise HTTPException('User not found')

    db.session.merge(user_load)
    db.session.commit()


def delete_user(user_id: int):
    '''Delete user'''

    db.session.merge(User(id=user_id, status='INACTIVE'))
    db.session.commit()
