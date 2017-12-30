import json

from flask import request, render_template, jsonify, abort

from utility import request_json, free_from_


def crud(blue, collection, skeleton):
    template_dir = blue.name
    '''
    @blue.route('/+', methods=['GET', 'POST'])
    @blue.route('/<_id>+', methods=['GET', 'POST'])
    def create(_id=None):
        if request.method == 'GET':
            return render_template(template_dir + '/+.html')
        if request.method == 'POST':
            document = {}
            if skeleton:
                from copy import deepcopy
                document = deepcopy(skeleton)
            try:
                _json = request_json(request)
                for key, value in _json.items():
                    sub_document, key = dot_notation(document, key)
                    sub_document[key] = value
            except:
                pass
            if _id:
                document['_id'] = ObjectId(_id)
            if current_user.is_authenticated:
                document['_author'] = current_user._id
            document['_date'] = datetime.datetime.now()

            result = collection.insert_one(str2obj(document))
            if 'insert' in redundancies:
                redundancies['insert'](document)

            return obj2str(result.inserted_id)
    '''

    @blue.route('/*', methods=['GET', 'POST'])
    def delete_all():
        collection.purge()
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

    '''
    @blue.route('/<_id>*', methods=['GET', 'POST'])
    def delete(_id):
        if 'delete' in redundancies:
            document = collection.find_one({'_id': ObjectId(_id)})
            redundancies['delete'](document)
        collection.delete_one({
            '_id': ObjectId(_id)
        })
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    '''
    '''
    @blue.route('/<_id>-<dash>', methods=['GET', 'POST'])
    @blue.route('/<_id>-', methods=['GET', 'POST'])
    def minimize(_id, dash=''):
        fields = []
        if 'p' in dash and projection:
            fields.append(projection)
        try:
            document = collection.find_one({'_id': ObjectId(_id)}, *fields)
            obj2str(document)
            return jsonify(document)
        except Exception as e:
            return str(e)
    '''

    @blue.route('/-')
    def minimize_all():
        return jsonify(collection.all())

    '''
    @blue.route('/<_id>')
    def get(_id):
        try:
            document = collection.find_one({'_id': ObjectId(_id)})
            document, ctx = load_document(document)
        except Exception as e:
            return str(e), 403
        return render_template(template + '.html', **document, **ctx)
    '''

    @blue.route('/<int:_id>.$$', methods=['GET', 'POST'])
    def universal_alter(_id):
        try:
            _json = request_json(request)
            _json = free_from_(_json)
            collection.update(_json, doc_ids=[_id])
            return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
        finally:
            document = collection.get(doc_id=_id)
            if not document:
                abort(406)
            return render_template('$$.html', ctx=document)

    '''
    @blue.route('/<_id>$')
    @blue.route('/<_id>$-<operator>')
    def alter(_id, operator):
        _id = ObjectId(_id)
        try:
            from pymongo import ReturnDocument
            if 'node' in request.values:
                _json = request_json(request, specific_type=None)
                node = request.values['node']
                if not _json:
                    document = collection.find_one_and_update(
                        {'_id': _id},
                        {'$unset': {node: ""}},
                        return_document=ReturnDocument.AFTER
                    )
                else:
                    document = collection.find_one_and_update(
                        {'_id': _id},
                        {'${}'.format(operator): {node: _json}},
                        return_document=ReturnDocument.AFTER
                    )
            else:
                _json = request_json(request)
                document = collection.find_one_and_update(
                    {'_id': _id},
                    {'$set': _json},
                    return_document=ReturnDocument.AFTER
                )
            if 'update' in redundancies:
                redundancies['update'](document)
            if 'ajax' in request.values:
                return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
        except Exception as e:
            print(e)
            try:
                document = collection.find_one({'_id': _id})
            except Exception as e:
                print(e)
                abort(405)
        document, ctx = load_document(document)
        return render_template(template + '_plus.html', **document, **ctx)
    '''
