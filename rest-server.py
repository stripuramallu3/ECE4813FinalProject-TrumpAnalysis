from __future__ import print_function
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask import render_template, redirect

import sys
import requests
import json

app = Flask(__name__, static_url_path="")


@app.route('/', methods=['GET'])
def home_page():
    return render_template("index.html")

@app.route('/distribution', methods=['GET'])
def view_distribution():
    results = requests.get("https://0qqnj9g8jh.execute-api.us-east-1.amazonaws.com/prod/getsentimentvalues").json()
    return render_template('distribution.html', data=results)

@app.route('/topten', methods=['GET'])
def view_topten():
    results = requests.get("https://0qqnj9g8jh.execute-api.us-east-1.amazonaws.com/prod/gettophashtags").json()
    
    return render_template('bubbles.html', data=json.dumps(results))

@app.route('/breakdown', methods=['GET'])
def view_breakdown(): 
    data = []
    negative = requests.get("https://0qqnj9g8jh.execute-api.us-east-1.amazonaws.com/prod/getnegativecount").json() 
    positive = requests.get("https://0qqnj9g8jh.execute-api.us-east-1.amazonaws.com/prod/getpositivecount").json()
    neutral = requests.get("https://0qqnj9g8jh.execute-api.us-east-1.amazonaws.com/prod/getneutralcount").json()
    data.append({"sala":"Positive", "value":positive})
    data.append({"sala":"Negative","value":negative})
    data.append({"sala":"Neutral", "value":neutral})
    return render_template('breakdown.html', data=data)










if __name__ == '__main__':
    app.run(host='0.0.0.0', port=170)

