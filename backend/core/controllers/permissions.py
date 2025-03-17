from apiflask import APIBlueprint


bp = APIBlueprint('permissions', __name__)


@bp.get('/')
def get_permissions():
    '''Get permissions'''
    pass


@bp.post('/')
def create_permissions():
    '''Create permissions'''
    pass


@bp.put('/')
def update_permissions():
    '''Update permissions'''
    pass


@bp.delete('/')
def delete_permissions():
    '''Delete permissions'''
    pass