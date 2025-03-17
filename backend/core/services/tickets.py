from core.app import db
from core.models import Ticket
from sqlalchemy import or_, and_
from werkzeug.exceptions import HTTPException


def get_tickets(search: str, page: int, per_page: int):
    '''Get tickets'''

    query = Ticket.status == 'ACTIVE'
    if search:
        query = and_(Ticket.status == 'ACTIVE',
                     or_(Ticket.name.ilike(f'%{search}%')))

    return db.paginate(db.session.query(Ticket).filter(query),
                       page=page, per_page=per_page)


def get_ticket(ticket_id: int):
    '''Get ticket by ticket id'''

    return db.session.query(Ticket).filter(Ticket.id == ticket_id).first()


def check_ticket_exists(ticket_id: int):
    '''Check if ticket exists'''

    return db.session.query(Ticket).filter(Ticket.id == ticket_id).first()


def update_ticket(ticket_id: int, ticket_load):
    '''Update ticket'''

    if not check_ticket_exists(ticket_id):
        raise HTTPException('Ticket not found')

    db.session.merge(ticket_load)
    db.session.commit()


def delete_ticket(ticket_id: int):
    '''Delete ticket'''

    db.session.merge(Ticket(id=ticket_id, status='INACTIVE'))
    db.session.commit()
