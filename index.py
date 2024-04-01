import flask
from flask_terminado import Terminal


app = flask.Flask(__name__)


@app.route('/')
def home():
    return 'home'


terminal = Terminal(app)
terminal.add_terminal('/bash', ['bash'])
