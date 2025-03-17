import os
from core.app import db
from core.models import Movie
from core.services import movies
from apiflask import APIBlueprint, abort
from werkzeug.utils import secure_filename
from core.schemas.utils import Message, Pagination
from core.schemas.movies import MovieIn, MovieOut, MoviesOut, MoviesCategoryOut


bp = APIBlueprint('movies', __name__)


@bp.get('/')
@bp.input(Pagination, location='query')
@bp.output(MoviesOut)
def get_movies(query_data):
    '''Get movies'''

    try:
        return {'items': movies.get_movies(query_data['search'],
                                           query_data['page'],
                                           query_data['per_page'])}
    except Exception as ex:
        abort(str(ex))


@bp.get('/<int:movie_id>')
@bp.output(MovieOut)
def get_movie(movie_id):
    '''Get movie'''

    try:
        return movies.get_movie(movie_id)
    except Exception as ex:
        abort(str(ex))


@bp.post('/')
@bp.input(MovieIn, location='form_and_files')
def create_movie(form_and_files_data):
    try:
        trailer_video_file = form_and_files_data['trailerVideo']

        trailer_video_filename = secure_filename(trailer_video_file.filename)
        trailer_video_file.save(os.path.join(
            './files', trailer_video_filename))

        name = form_and_files_data['name']
        classification_age = form_and_files_data['classification_age']
        duration_minutes = form_and_files_data['duration_minutes']
        category_id = form_and_files_data['category_id']
        trailer_video = f'files/{trailer_video_filename}'

        movie_loaded = Movie(name=name, duration_minutes=duration_minutes,
                             classification_age=classification_age,
                             trailer_video=trailer_video,
                             category_id=category_id)
        db.session.add(movie_loaded)
        db.session.commit()

        return {'message': 'Movie created succesfully'}
    except Exception as ex:
        print(str(ex))
        abort(str(ex))


@bp.put('/<int:movie_id>')
@bp.input(MovieIn, location='form_and_files')
@bp.output(Message)
def update_movies(movie_id, form_and_files_data):
    '''Update movie'''

    try:
        name = form_and_files_data['name']
        classification_age = form_and_files_data['classification_age']
        duration_minutes = form_and_files_data['duration_minutes']
        category_id = form_and_files_data['category_id']

        if 'trailerVideo' in form_and_files_data:
            trailer_video_file = form_and_files_data['trailerVideo']
            trailer_video_filename = secure_filename(trailer_video_file.filename)
            trailer_video_file.save(os.path.join(
                './files', trailer_video_filename))
            trailer_video = f'files/{trailer_video_filename}'


            movie_loaded = Movie(id=movie_id, name=name, duration_minutes=duration_minutes,
                             classification_age=classification_age,
                             trailer_video=trailer_video,
                             category_id=category_id)
        else:
            movie_loaded = Movie(id=movie_id, name=name, duration_minutes=duration_minutes,
                            classification_age=classification_age,
                            category_id=category_id)
        
        db.session.merge(movie_loaded)
        db.session.commit()

        return {'message': 'movie updated successfuly'}
    except Exception as ex:
        print(str(ex))
        abort(str(ex))

@bp.get('/category/<int:category_id>')
@bp.output(MoviesCategoryOut)
def get_movies_by_category(category_id):
    try:
        movies = db.session.query(Movie).filter(Movie.category_id == category_id).all()
        print('MOVIES: ')
        print(movies[0].trailer_video)
        return{'items': movies}
    except Exception as ex:
        print(str(ex))
        abort(str(ex))


@bp.delete('/<int:movie_id>')
@bp.output(Message)
def delete_movies(movie_id):
    '''Delete movies'''

    try:
        movies.delete_movie(movie_id)
        return {'message': 'movie deleted successfuly'}
    except Exception as ex:
        print(str(ex))
        abort(str(ex))
