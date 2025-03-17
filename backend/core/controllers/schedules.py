from core.app import db
from core.models import Schedule
from core.services import schedules
from apiflask import APIBlueprint, abort
from core.schemas.utils import Message, Pagination
from core.schemas.schedules import ScheduleIn, ScheduleOut, SchedulesOut


bp = APIBlueprint('schedules', __name__)


@bp.get('/')
@bp.input(Pagination, location='query')
@bp.output(SchedulesOut)
def get_schedules(query_data):
    '''Get schedules'''

    try:
        return {'items': schedules.get_schedules(query_data['search'], 
                                         query_data['page'],
                                         query_data['per_page'])}
    except Exception as ex:
        abort(str(ex))


@bp.get('/<int:schedule_id>')
@bp.output(ScheduleOut)
def get_schedule(schedule_id):
    '''Get schedule'''

    try:
        return schedules.get_schedule(schedule_id)
    except Exception as ex:
        abort(str(ex))


@bp.put('/<int:schedule_id>')
@bp.input(ScheduleIn)
@bp.output(Message)
def update_schedules(schedule_id, json_data):
    '''Update schedule'''
    
    try:
        schedules.update_schedule(schedule_id, json_data)
        return {'message': 'schedule updated successfuly'}
    except Exception as ex:
        print(str(ex))
        abort(str(ex))


@bp.delete('/<int:schedule_id>')
@bp.output(Message)
def delete_schedules(schedule_id):
    '''Delete schedules'''

    try:
        schedules.delete_schedule(schedule_id)
        return {'message': 'schedule deleted successfuly'}
    except Exception as ex:
        print(str(ex))
        abort(str(ex))
