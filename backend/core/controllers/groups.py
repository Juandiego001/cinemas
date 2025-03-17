from apiflask import APIBlueprint


bp = APIBlueprint('groups', __name__)


@bp.get('/')
def get_users():
    '''Get groups'''
    pass


@bp.post('/')
def create_users():
    '''Create groups'''
    pass


@bp.put('/')
def update_users():
    '''Update groups'''
    pass


@bp.delete('/')
def delete_users():
    '''Delete groups'''
    pass