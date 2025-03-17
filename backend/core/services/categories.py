from core.app import db
from core.models import Category
from sqlalchemy import or_, and_
from werkzeug.exceptions import HTTPException


def get_categories(search: str, page: int, per_page: int):
    '''Get categories'''

    query = Category.status == 'ACTIVE'
    if search:
        query = and_(Category.status == 'ACTIVE',
                     or_(Category.name.ilike(f'%{search}%')))

    return db.paginate(db.session.query(Category).filter(query),
                       page=page, per_page=per_page)


def get_category(category_id: int):
    '''Get category by category id'''

    return db.session.query(Category).filter(Category.id == category_id).first()


def check_category_exists(category_id: int):
    '''Check if category exists'''

    return db.session.query(Category).filter(Category.id == category_id).first()


def update_category(category_id: int, category_load):
    '''Update category'''

    if not check_category_exists(category_id):
        raise HTTPException('Category not found')

    db.session.merge(category_load)
    db.session.commit()


def delete_category(category_id: int):
    '''Delete category'''

    db.session.merge(Category(id=category_id, status='INACTIVE'))
    db.session.commit()
