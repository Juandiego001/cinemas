from flask import send_file
from apiflask import APIBlueprint, abort
from werkzeug.utils import secure_filename


bp = APIBlueprint('files', __name__)


@bp.get('/<string:file_name>')
def get_file(file_name):
    try:
        print('FILE NAME: ', file_name)
        if file_name:
            return send_file(f'./files/{file_name}')
        else:
            return {}
    except Exception as ex:
        print(str(ex))
        abort(str(ex))
