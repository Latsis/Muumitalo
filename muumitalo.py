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
            'answer': "Muumipappa has gone crazy. He is blocking the door and won't let anyone inside unless you guess his favourite drink right. I know it is vaapukkamehu but I guess after he read all those hacker books he modified the spelling somehow. Go there and bombard him with answers until he lets you in! He is located at localhost:5000/ovi/"
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
        if 'va4PukK4M3HU' in dataDict['answer']:
            data = {
            'Muumi'  : 'MuumiPappa',
            'answer' : 'Wonderful! Come in and taste some of my va4PukK4M3HU'
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
            'answer' : 'What is the haczor name for my favourite drink?'
           }
        js = json.dumps(data)
        
        resp = Response(js, status=200, mimetype='application/json')
        return resp



    


    
    
