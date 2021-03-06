from ast import literal_eval
from functools import wraps
from flask import abort
from config import current_user


def request_json(request, _json=None, specific_type=dict):
    raw = None
    if _json:
        raw = _json
    elif 'json' in request.values:
        raw = request.values['json']
    else:
        raise Exception
    try:
        evaluated = literal_eval(raw)
        if type(evaluated) is dict:
            for key, value in request.values.items():
                if 'json.' in key:
                    key = '.'.join(key.split('.')[1:])
                    evaluated, key = dot_notation(evaluated, key)
                    try:
                        evaluated[key] = literal_eval(value)
                    except:
                        evaluated[key] = value
        if specific_type and type(evaluated) is specific_type:
            return evaluated
        elif not specific_type:
            return evaluated
        else:
            raise Exception
    except Exception as e:
        return raw


def request_attributes(request, **kwargs):
    values = request.values
    _json = {}
    for kay, _type in kwargs.items():
        if kay not in values:
            raise AttributeError()
        else:
            value = values[kay]
            if _type is str:
                evaluated_value = value
            else:
                evaluated_value = literal_eval(value)
                if type(evaluated_value) is not _type:
                    raise TypeError()
            _json[kay] = evaluated_value
    return _json


def free_from_(tree):
    if isinstance(tree, dict):
        new_tree = {}
        for k, node in tree.items():
            if '__' not in k:
                new_tree[k] = free_from_(node)
        return new_tree
    elif isinstance(tree, list):
        for idx, node in enumerate(tree):
            tree[idx] = free_from_(node)
    return tree


def dot_notation(_dict, key):
    keys = key.split('.')
    for key in keys[:-1]:
        if key not in _dict:
            _dict[key] = {}
        _dict = _dict[key]
    return _dict, keys[-1]


def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not current_user['is_authenticated']:
            abort(401)
        return func(*args, **kwargs)
    return decorated_function
