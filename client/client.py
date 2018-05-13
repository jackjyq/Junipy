from flask import Flask,jsonify, url_for, Response, render_template, make_response, redirect
from flask_restful import reqparse, request
import requests,html,urllib.parse
import base64

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def lga():
	return render_template('index.html'), 200

if __name__ == "__main__":
	app.config['JSON_AS_ASCII'] = False
	app.run(debug=True , port=5001)
	