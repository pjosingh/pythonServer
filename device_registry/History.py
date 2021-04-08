from flask_restful import Resource, Api, reqparse

class History(Resource):
    def get(self):
        response=""
        file=open("./history.txt", "r")
        count = 50
        for line in file:
            if count == 0:
                return {'message': 'Success', 'data': response}
            response = response + line+"\n"
            count = count - 1
        return {'message': 'Success', 'data': response}