from core.app import db
from core.models import Movie
from sqlalchemy import or_, and_
from werkzeug.exceptions import HTTPException


def get_movies(search: str, page: int, per_page: int):
    '''Get movies'''

    query = Movie.status == 'ACTIVE'
    if search:
        query = and_(Movie.status == 'ACTIVE',
                     or_(Movie.name.ilike(f'%{search}%')))

    return db.paginate(db.session.query(Movie).filter(query),
                       page=page, per_page=per_page)


def get_movie(movie_id: int):
    '''Get movie by movie id'''

    return db.session.query(Movie).filter(Movie.id == movie_id).first()


def check_movie_exists(movie_id: int):
    '''Check if movie exists'''

    return db.session.query(Movie).filter(Movie.id == movie_id).first()


def update_movie(movie_id: int, movie_load):
    '''Update movie'''

    if not check_movie_exists(movie_id):
        raise HTTPException('Movie not found')

    db.session.merge(movie_load)
    db.session.commit()


def delete_movie(movie_id: int):
    '''Delete movie'''

    db.session.merge(Movie(id=movie_id, status='INACTIVE'))
    db.session.commit()
