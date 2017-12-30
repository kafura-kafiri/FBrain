from flask import Flask, render_template
from config import current_user

app = Flask(__name__)


from crud import *
import importlib
crud_names = list(globals().keys())


for name in crud_names:
    variable = globals()[name]
    if isinstance(variable, Blueprint):
        importlib.import_module('crud.' + name)
        app.register_blueprint(variable)


@app.route('/')
def index():
    return render_template('index.html', current_user=current_user)


if __name__ == '__main__':
    app.run(debug=True)