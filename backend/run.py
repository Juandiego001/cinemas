from core.app import app, HOST, PORT
from core.controllers.users import bp as bp_users
from core.controllers.groups import bp as bp_groups
from core.controllers.permissions import bp as bp_permissions
from core.controllers.modules import bp as bp_modules
from core.controllers.categories import bp as bp_categories
from core.controllers.tickets import bp as bp_tickets
from core.controllers.schedules import bp as bp_schedules
from core.controllers.chairs import bp as bp_chairs
from core.controllers.rooms import bp as bp_rooms
from core.controllers.movies import bp as bp_movies
from core.controllers.files import bp as bp_files


app.register_blueprint(bp_users, url_prefix='/api/users')
app.register_blueprint(bp_groups, url_prefix='/api/groups')
app.register_blueprint(bp_modules, url_prefix='/api/modules')
app.register_blueprint(bp_permissions, url_prefix='/api/permissions')
app.register_blueprint(bp_categories, url_prefix='/api/categories')
app.register_blueprint(bp_tickets, url_prefix='/api/tickets')
app.register_blueprint(bp_schedules, url_prefix='/api/schedules')
app.register_blueprint(bp_chairs, url_prefix='/api/chairs')
app.register_blueprint(bp_rooms, url_prefix='/api/rooms')
app.register_blueprint(bp_movies, url_prefix='/api/movies')
app.register_blueprint(bp_files, url_prefix='/api/files')


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)
