from crud import user


@user.route('/signup/<id>')
def signup(_id):
    print(_id)

@user.route('/login/<id>')
def login(_id):
    pass

@user.route('/logout')
def logout():
    pass