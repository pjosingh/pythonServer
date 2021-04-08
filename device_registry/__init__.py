from flask import Flask,g
from flask_restful import Resource, Api, reqparse
import markdown
import os
import shelve
from flask_cors import CORS

from device_registry.History import History
from device_registry.GoodOrBad import GoodOrBad
from device_registry.DeviceList import DeviceList
from device_registry.RegisterNewTracker import RegisterNewTracker

app = Flask(__name__)
CORS(app)
# Create the API
api = Api(app)

def get_db():
    db = getattr(g,'_database', None)
    if db is None:
        db = g._database = shelve.open("devices.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello():
    with open(os.path.dirname(app.root_path)+ "/readme.md") as f:
        c = f.read()
        return markdown.markdown(c)



api.add_resource(DeviceList, '/devices')
api.add_resource(History, '/history')
api.add_resource(GoodOrBad, '/gb')
api.add_resource(RegisterNewTracker, '/register')
