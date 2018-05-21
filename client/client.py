from flask import Flask,jsonify, url_for, Response, render_template, make_response, redirect
from flask_restful import reqparse, request
import requests,html,urllib.parse
import base64, json, requests

app = Flask(__name__)
flagList = []

apiBase = "http://127.0.0.1:5000"

def loadCountryFlag():
	with open('./static/data/country_flags.json') as json_data:
		return json.load(json_data)
		
@app.route('/', methods=['POST','GET'])
def home():
	flagList = loadCountryFlag()
#	print(len(flagList))
	return render_template('home.html', flagList=flagList), 200

@app.route('/<country>', methods=['POST','GET'])
def detail(country):
	response = requests.get(apiBase+"/detail/"+country)
	country = json.loads(response.text)
	return render_template('detail.html', country=country), 200

@app.route('/analysis', methods=['POST','GET'])
def analysis():
#	response = requests.get(apiBase+"/analysis/")
#	country = json.loads(response.text)
	return render_template('analysis.html'), 200

if __name__ == "__main__":
	app.config['JSON_AS_ASCII'] = False
	app.run(debug=True , port=5001)
	