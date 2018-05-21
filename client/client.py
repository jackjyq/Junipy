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
		
@app.route('/', methods=['GET'])
def home():
	response = requests.get(apiBase+"/home")
	dict = json.loads(response.text)
	print(dict['flags'])
#	flagList = loadCountryFlag()
#	print(flagList)
	return render_template('home.html', GDP=dict['GDP'],flagList=dict['flags']), 200

#@app.route('/<country>', methods=['GET'])
#def detail(country):
#	response = requests.get(apiBase+"/detail/"+country)
#	country = json.loads(response.text)
#	return render_template('detail.html', country=country), 200

@app.route('/test/analysis', methods=['GET'])
def analysis():
	data = loadCountryFlag()
#	response = requests.get(apiBase+"/analysis/")
#	country = json.loads(response.text)
#	return render_template('analysis.html', data=data), 200
	return render_template('analysis.html'), 200

if __name__ == "__main__":
	app.config['JSON_AS_ASCII'] = False
	app.run(debug=True , port=5001)
	