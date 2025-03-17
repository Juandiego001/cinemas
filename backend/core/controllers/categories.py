from core.app import db
from core.models import Category
from core.services import categories
from apiflask import APIBlueprint, abort
from core.schemas.utils import Message, Pagination
from core.schemas.categories import CategoryIn, CategoryOut, CategoriesOut


bp = APIBlueprint('categories', __name__)


@bp.get('/')
@bp.input(Pagination, location='query')
@bp.output(CategoriesOut)
def get_categories(query_data):
    '''Get categories'''

    try:
        return {'items': categories.get_categories(query_data['search'], 
                                         query_data['page'],
                                         query_data['per_page'])}
    except Exception as ex:
        abort(str(ex))


@bp.get('/<int:category_id>')
@bp.output(CategoryOut)
def get_category(category_id):
    '''Get category'''

    try:
        return categories.get_category(category_id)
    except Exception as ex:
        abort(str(ex))


@bp.post('/')
@bp.input(CategoryIn, arg_name='category')
@bp.output(Message)
def create_category(category):
    '''Create category'''

    try:
        db.session.add(category)
        db.session.commit()
        return {'message': 'Category created successfuly'}
    except Exception as ex:
        print(str(ex))
        abort(str(ex))


@bp.put('/<int:category_id>')
@bp.input(CategoryIn)
@bp.output(Message)
def update_categories(category_id, json_data):
    '''Update category'''

    try:
        categories.update_category(category_id, json_data)
        return {'message': 'category updated successfuly'}
    except Exception as ex:
        print(str(ex))
        abort(str(ex))


@bp.delete('/<int:category_id>')
@bp.output(Message)
def delete_categories(category_id):
    '''Delete categories'''

    try:
        categories.delete_category(category_id)
        return {'message': 'category deleted successfuly'}
    except Exception as ex:
        print(str(ex))
        abort(str(ex))
