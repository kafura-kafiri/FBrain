from crud import user
from config import users
from tinydb import Query

default = {
    'name': 'unanimous',
    'id': '',
}

current_user = {}


@user.route('/signup/<id>')
def signup(_id):
    new_user = default.copy()
    new_user['id'] = _id
    users.insert(new_user)


@user.route('/login/<id>')
def login(_id):
    User = Query()
    current_user = users.search(User.id == _id)
    current_user['is_authenticated'] = True


@user.route('/logout')
def logout():
    current_user.clear()
    current_user['is_authenticated'] = False

logout()