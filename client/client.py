from flask import Flask,jsonify, url_for, Response, render_template, make_response, redirect
from flask_restful import reqparse, request
import requests,html,urllib.parse
import base64, json

app = Flask(__name__)
flagList = []

def loadCountryFlag():
	with open('./static/data/country_flags.json') as json_data:
		return json.load(json_data)
		
@app.route('/', methods=['POST','GET'])
def lga():
	flagList = loadCountryFlag()
	print(len(flagList))
	return render_template('index.html', flagList=flagList), 200

if __name__ == "__main__":
	app.config['JSON_AS_ASCII'] = False
	app.run(debug=True , port=5001)
	