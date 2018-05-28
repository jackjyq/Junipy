from flask import Flask,jsonify, url_for, Response, render_template, make_response, redirect
from flask_restful import reqparse, request
import requests,html,urllib.parse
import base64, json, requests

app = Flask(__name__)
flagList = []

apiBase = "http://127.0.0.1:5000"

regionDict = {"Asia":"asia_en",
			  "Africa":"africa_en",
			  "Oceania":"australia_en",
			  "Americas":"north-america_en",
			  "Europe":"europe_en",
			  "World":"world_en"}

def regionMapping(region):
	if region in regionDict:
		return regionDict[region]
	return "world_en"

def loadCountryFlag():
	with open('./static/data/country_flags.json') as json_data:
		return json.load(json_data)
		
@app.route('/', methods=['GET'])
def home():
	response = requests.get(apiBase+"/home")
	dict = json.loads(response.text)
	return render_template('index.html', GDP=dict['GDP'],flagList=dict['flags']), 200

@app.route('/<country>', methods=['GET'])
@app.route('/<country>/<target>', methods=['GET'])
def detail(country,target='GDP'):
	response = requests.get(apiBase+"/detail/"+country.upper())
	data = json.loads(response.text)
	for key in ['GDP', 'agriculture', 'industry', 'service', 'population','PM25Index']:
		key = key + 'History'
		for dict in data[key]['data']:
			if dict['value'] == None:
				continue
			dict['value'] = float(dict['value'])
	return render_template('detail.html', country=data, code=country, target=target), 200

@app.route('/analysis', methods=['GET'])
def analysis():
	data = loadCountryFlag()
	return render_template('analysis.html'), 200

@app.route('/region/<region>', methods=['GET'])
def region(region):
	response = requests.get(apiBase+"/region/"+region)
	country = json.loads(response.text)
	map_type = regionMapping(region)
	return render_template('regoin.html', region=map_type,country=country), 200

if __name__ == "__main__":
	app.config['JSON_AS_ASCII'] = False
	app.run(debug=True , port=5001)
	