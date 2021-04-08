from flask_restful import Resource, reqparse
from flask import Flask,g


import shelve
def get_db():
    db = getattr(g,'_database', None)
    if db is None:
        db = g._database = shelve.open("tracker.db")
    return db


class RegisterNewTracker(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('operation', required=True)
        parser.add_argument('name', required=True)
        # Parse the arguments into an object
        args = parser.parse_args()

        if args['operation'] == "ADD_TRACKER":
            name = args['name']
            db = get_db()
            db[args['name']] = "active"
            # PersonEncoder().encode(person)
            return {'message': 'Success', 'data': 'added'}
        return {'message': 'Success', 'data': "Unknown operation"}

    def get(self):
        db = get_db()
        keys = list(db.keys())
        response = ""
        for key in keys:
            response = response+key+"<br>"
        return {'message': 'Success', 'data': response}