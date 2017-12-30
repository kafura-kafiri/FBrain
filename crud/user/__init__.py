from crud import user
from config import users, current_user
from tinydb import where
from crud.crud import crud
import json
from utility import login_required
from flask import url_for, redirect
from crud.csv.uart import thread

default = {
    'name': 'unanimous',
}


@user.route('/signup/<name>')
def signup(name):
    new_user = default.copy()
    new_user['name'] = name
    users.insert(new_user)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@user.route('/login/<name>')
def login(name=None):
    _user = users.get(where('name') == name)
    current_user.update(_user)
    current_user['is_authenticated'] = True
    current_user['_id'] = _user.doc_id
    thread.is_alive = False
    return redirect(url_for('index'))


@user.route('/logout')
@login_required
def logout():
    name = current_user['name']
    current_user.clear()
    current_user['is_authenticated'] = False
    thread.is_alive = False
    return redirect(url_for('index'))


crud(user, users, default)