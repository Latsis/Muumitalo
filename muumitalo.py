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
            'answer': "Muumipappa has gone crazy. He is blocking the door and won't let anyone inside unless you guess his favourite song. I know it's that one hockey song he's been playing non stop but I guess after he watched all those hacker movies he modified the spelling somehow. Go there and bombard him with answers until he lets you in! He is located at localhost:5000/ovi/"
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
        if 'lOiK0m0rkos1saan' in dataDict['answer']:
            data = {
            'Muumi'  : 'MuumiPappa',
            'answer' : 'Wonderful! Come in and listen to these awesome tunes with me!'
            }
            js = json.dumps(data)
            print request.data        
            resp = Response(js, status=200, mimetype='application/json')
            return resp
        else:
            data = {
            'Muumi'  : 'MuumiPappa',
            'answer' : 'That is not it!'
            }
            js = json.dumps(data)
            print request.data
            resp = Response(js, status=404, mimetype='application/json')
            return resp            
    else:
        data = {
            'Muumi'  : 'MuumiPappa',
            'answer' : 'What is the haxxor name of my favourite song?'
           }
        js = json.dumps(data)
        
        resp = Response(js, status=200, mimetype='application/json')
        return resp
