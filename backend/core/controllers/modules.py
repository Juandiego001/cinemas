from apiflask import APIBlueprint


bp = APIBlueprint('modules', __name__)


@bp.get('/')
def get_modules():
    '''Get modules'''
    pass


@bp.post('/')
def create_modules():
    '''Create modules'''
    pass


@bp.put('/')
def update_modules():
    '''Update modules'''
    pass


@bp.delete('/')
def delete_modules():
    '''Delete modules'''
    pass