from core.app import db
from core.models import Schedule
from sqlalchemy import or_, and_
from werkzeug.exceptions import HTTPException


def get_schedules(search: str, page: int, per_page: int):
    '''Get schedules'''

    query = Schedule.status == 'ACTIVE'
    if search:
        query = and_(Schedule.status == 'ACTIVE',
                     or_(Schedule.name.ilike(f'%{search}%')))

    return db.paginate(db.session.query(Schedule).filter(query),
                       page=page, per_page=per_page)


def get_schedule(schedule_id: int):
    '''Get schedule by schedule id'''

    return db.session.query(Schedule).filter(Schedule.id == schedule_id).first()


def check_schedule_exists(schedule_id: int):
    '''Check if schedule exists'''

    return db.session.query(Schedule).filter(Schedule.id == schedule_id).first()


def update_schedule(schedule_id: int, schedule_load):
    '''Update schedule'''

    if not check_schedule_exists(schedule_id):
        raise HTTPException('Schedule not found')

    db.session.merge(schedule_load)
    db.session.commit()


def delete_schedule(schedule_id: int):
    '''Delete schedule'''

    db.session.merge(Schedule(id=schedule_id, status='INACTIVE'))
    db.session.commit()
