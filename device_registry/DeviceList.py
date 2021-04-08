from flask_restful import Resource
from yahoo_fin import stock_info
import math


def line_prepender(filename, line):
    try:
        with open(filename, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(line.rstrip('\r\n') + '\n' + content)
    except:
        with open(filename, 'w+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(line.rstrip('\r\n') + '\n' + content)

class DeviceList(Resource):
    def get(self):

        price_fb = stock_info.get_live_price("FB")
        price_tsla = stock_info.get_live_price("TSLA")
        price_fb =math.trunc(price_fb)
        price_tsla = math.trunc(price_tsla)
        response = "<table style='width:100%;background-color:#ede9e9;border:1px;'><tr><td>" + str(price_fb) + "</td><td>" + str(price_tsla) + "</td></table>"
        line_prepender("./history.txt", response+"\n")
        return {'message': 'Success', 'data': response}