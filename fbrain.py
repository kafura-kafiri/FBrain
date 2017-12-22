from flask import Flask, render_template, Blueprint

app = Flask(__name__)


from crud import *
import importlib
crud_names = list(globals().keys())


for name in crud_names:
    variable = globals()[name]
    if isinstance(variable, Blueprint):
        importlib.import_module('crud.' + name)
        app.register_blueprint(variable)


if __name__ == '__main__':
    app.run(debug=True)