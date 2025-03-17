from core.app import db
from core.models import Ticket
from core.services import tickets
from apiflask import APIBlueprint, abort
from core.schemas.utils import Message, Pagination
from core.schemas.tickets import TicketIn, TicketOut, TicketsOut


bp = APIBlueprint('tickets', __name__)


@bp.get('/')
@bp.input(Pagination, location='query')
@bp.output(TicketsOut)
def get_tickets(query_data):
    '''Get tickets'''

    try:
        return {'items': tickets.get_tickets(query_data['search'], 
                                         query_data['page'],
                                         query_data['per_page'])}
    except Exception as ex:
        abort(str(ex))


@bp.get('/<int:ticket_id>')
@bp.output(TicketOut)
def get_ticket(ticket_id):
    '''Get ticket'''

    try:
        return tickets.get_ticket(ticket_id)
    except Exception as ex:
        abort(str(ex))


@bp.put('/<int:ticket_id>')
@bp.input(TicketIn)
@bp.output(Message)
def update_tickets(ticket_id, json_data):
    '''Update ticket'''
    
    try:
        tickets.update_ticket(ticket_id, json_data)
        return {'message': 'ticket updated successfuly'}
    except Exception as ex:
        print(str(ex))
        abort(str(ex))


@bp.delete('/<int:ticket_id>')
@bp.output(Message)
def delete_tickets(ticket_id):
    '''Delete tickets'''

    try:
        tickets.delete_ticket(ticket_id)
        return {'message': 'ticket deleted successfuly'}
    except Exception as ex:
        print(str(ex))
        abort(str(ex))
