from flask import Flask
from flask import Response
from flask import request
from flask import json
from flask import render_template
app = Flask(__name__)



@app.route('/')
def portaat():
    data = {
            'Muumi'  : 'Muumimamma',
            'answer': 'Muumipappa has gone crazy. He is blocking the door and won\'t let anyone inside unless you guess where he wants to go. I know he would like to go back to the market square, but I guess after watching all those hacker movies he is expecting a little twist to the name of the place. Go there and bombard him with answers until he comes out! He is located at localhost:5000/ovi/'
            }
    js = json.dumps(data)
        
    resp = Response(js, status=200, mimetype='application/json')
    return resp

@app.route('/ovi/', methods=["GET","POST"])
def ovi():
    if request.method == 'POST':
        data = request.data
        dataDict = json.loads(data)
        print dataDict
        if 'Tor1lL3' in dataDict['answer']:
            data = {
            'Muumi'  : 'MuumiPappa',
            'answer' : 'W0nd3rful! Let\'s go!
            }
            js = json.dumps(data)
            print request.data        
            resp = Response(js, status=200, mimetype='application/json')
            return resp
        else:
            data = {
            'Muumi'  : 'MuumiPappa',
            'answer' : 'Th4t is n0t it!'
            }
            js = json.dumps(data)
            print request.data
            resp = Response(js, status=404, mimetype='application/json')
            return resp            
    else:
        data = {
            'Muumi'  : 'MuumiPappa',
            'answer' : 'Wh3r3 sh0uld w3 g0 t0 c3l3br4t3?'
           }
        js = json.dumps(data)
        
        resp = Response(js, status=200, mimetype='application/json')
        return resp
