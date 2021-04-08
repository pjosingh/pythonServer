from flask_restful import Resource
from yahoo_fin import stock_info

class GoodOrBad(Resource):
    def get(self):
        price_fb = 255
        cur_fb = stock_info.get_live_price("FB")
        price_t=563
        cur_tsla = stock_info.get_live_price("TSLA")

        fb=""
        if (int(cur_fb) - price_fb < 15):
            fb="GOOD"

        else:
            fb="BAD"

        tsla = ""
        if (int(cur_tsla) - price_t < 15):
            tsla = "GOOD"

        else:
            tsla = "BAD"

        response = "<table style='width:100%;background-color:gray'><tr><td>"+fb+"</td><td>"+tsla+"</td></table>"
        return {'message': 'Success', 'data': response}