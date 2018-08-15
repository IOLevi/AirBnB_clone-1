
#!/usr/bin/python3
#starts a Flask web application
import os
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def tear_down(exception):
    "tear down the storage"
    storage.close()

@app.route('/states_list', strict_slashes = False)
def state_list():
    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        # oddly, FS is set up to take all with a class, and DB with a string that
        # gets converted. Should mention this to them
        a = storage.all(State)
    else:
        a = storage.all("State")
    a = list(a.values())
    def sortfunc(e):
        return e.name
    a.sort(key=sortfunc)

    return render_template('7-states_list.html', a=a)

@app.route('/cities_by_states', strict_slashes = False)
def city_by_state():
    "prints city by state"
    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        a = storage.all(State)
    else:
        a = storage.all("State")

    a = list(a.values())
    return render_template('8-cities_by_states.html', a=a)

@app.route('/states', strict_slashes = False)
def get_state():
    "display an html page with all states in dbstorage"

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        a = storage.all(State)
    else:
        a = storage.all("State")

    a = list(a.values())
    return render_template('9-states.html', a=a)


@app.route('/states/<path:id>', strict_slashes = False)
def get_state_id(id):
    "displays an html page if id found"

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        a = storage.all(State)
    else:
        a = storage.all("State")

    a = list(a.values())
    b = []

    # only take the states that match the input id
    for state in a:
        if state.id == id:
            b.append(state)

    return render_template('9-states.html', b=b)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
