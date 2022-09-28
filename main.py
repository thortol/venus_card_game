import flask
from classes import GameInstance

temp = GameInstance()
app = flask.Flask(__name__)

@app.route('/')
def root():
    return "It works"

@app.route('/get_display/<int:id>')
def get_display(id):
    return temp.show_info(id)

if '__main__' == __name__:
    app.run(port=12345,debug=True)