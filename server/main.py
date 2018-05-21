import model
from mongoengine import connect
from collections import defaultdict
from server_config import *
from flask import Flask,jsonify,Response,send_file
import json
import math

global_indicator = {"GDP_total": "GDP",
                    "GDP_agriculture": "agriculture",
                    "GDP_industry": "industry",
                    "GDP_service": "service",
                    "CO2_emission": "CO2",
                    "PM25_index": "PM25Index",
                    "freshwater_withdrawals": "freshwaterWithdrawals",
                    "Population": "population"
                    }

country_change_code = {}
for i in global_codes:
	shorts = global_codes[i]['iso2']	
	country_change_code[shorts] = i

def loadCountryFlags():
 with open('./static/country_flags.json') as json_data:	 
	
   return json.load(json_data)

app = Flask(__name__)



@app.route('/home', methods=['GET'])
def get_home_data():
	alldata = {}
	data_dict = model.query(OVERVIEW, 'lastest_GDP')
	data_remove = data_dict.copy()
	for i in data_dict:
		if data_dict[i] == None:
			data_dict[i] = 0
			data_remove.pop(i)
		else:
			shorts = global_codes[i]["iso2"]
			data_remove[shorts] = data_remove.pop(i)
			data_remove[shorts] = float(data_dict[i])
	data_sort = sorted(data_remove.items(), key=lambda d:d[0])
	data_sorted = defaultdict()
	for i in data_sort:
		data_sorted[i[0]] = i[1]
	alldata['GDP'] = data_sorted
	alldata['flags'] = []
	flags_data = loadCountryFlags()
	flags = []
	#print(flags_data)
	for i in flags_data:
		short_code = i['code']
		if short_code in country_change_code:
			code = country_change_code[short_code]
			flagsdata1 = {'name':i['name'],'flag':i['flag'],'code':i['code']}
			alldata['flags'].append(flagsdata1)	
	a  = json.dumps(alldata)
	return a


@app.route('/GDP', methods=['GET'])
def get_lastest_GDP():
	data_dict = model.query(OVERVIEW, 'lastest_GDP')
	data_remove = data_dict.copy()
	for i in data_dict:
		if data_dict[i] == None:
			data_dict[i] = 0
			data_remove.pop(i)
		else:
			shorts = global_codes[i]["short"]
			data_remove[shorts] = data_remove.pop(i)
			data_remove[shorts] = float(data_dict[i])
	data_sort = sorted(data_remove.items(), key=lambda d:d[0])
	data_sorted = defaultdict()
	for i in data_sort:
		data_sorted[i[0]] = i[1]
	a  = json.dumps(data_sorted)
	return a


@app.route('/sortedGDP', methods=['GET'])
def get_sorted_GDP():
	data_dict = model.query(OVERVIEW, 'lastest_GDP')
	data_remove = data_dict.copy()
	for i in data_dict:
		if data_dict[i] == None:
			data_dict[i] = 0
			data_remove.pop(i)
		else:
			shorts = global_codes[i]["short"]
			data_remove[shorts] = data_remove.pop(i)
			data_remove[shorts] = float(data_dict[i])
	data_sort = sorted(data_remove.items(), key=lambda d:d[0])
	data_sorted = defaultdict()
	for i in data_sort:
		data_sorted[i[0]] = i[1]
	max_dict = sorted(data_remove.items(),key = lambda d:d[1],reverse = True)[0][1]
	min_dict = sorted(data_remove.items(),key = lambda d:d[1],reverse = True)[-1][1]
	log_dict = data_sorted
	for i in data_sorted:
		base = math.log(data_sorted[i])
		x = (base - math.log(min_dict))/(math.log(max_dict) - math.log(min_dict))
		log_dict[i] = x
	a  = json.dumps(log_dict)
	return a


@app.route("/detail/<code>",methods = ["GET"])
def get_detail(code):
	code = country_change_code[code]
	data_detail = {}
	data_detail['name'] = global_codes[code]['name']
	data_detail['introduction'] = model.query(INTRODUCTION, code)
	flag_prefix = 'https://www.cia.gov/library//publications/'\
                  + 'the-world-factbook/graphics/flags/large/'
	flag_suffix = '-lgflag.gif'
	short_code = global_codes[code]['short'].lower()
	flag_url = flag_prefix + short_code + flag_suffix
	data_detail['flag'] = flag_url
	for i in global_indicator:
		n = global_indicator[i]
		data_detail[n] = model.query(INDICATOR, code)['2016'][i]
		data_detail[global_indicator[i]+'History'] = []
	raw_data = model.query(INDICATOR, code)
	for i in range(1990,2017):
		year = str(i)
		for j in raw_data[year]:
			da = {'year':year,'value':raw_data[year][j]}
			key = global_indicator[j] + 'History'
			data_detail[key].append(da)
	return json.dumps(data_detail)



@app.route("/flags",methods = ["GET"])
def get_flags():
	flags = {}
	for i in global_codes:
		country_name = global_codes[i]['name']
		flag_prefix = 'https://www.cia.gov/library//publications/'\
                  + 'the-world-factbook/graphics/flags/large/'
		flag_suffix = '-lgflag.gif'
		short_code = global_codes[i]['short'].lower()
		flag_url = flag_prefix + short_code + flag_suffix
		flags[country_name] = flag_url
	return json.dumps(flags)


if __name__ == "__main__":
	db_client = connect(host=DB_URL)
	app.run()
	#app.run()
	# data_detail = {}
	# for i in global_indicator:
	# 	n = global_indicator[i]
	# 	data_detail[n] = model.query(INDICATOR, 'CHN')['2016'][i]
	# 	data_detail[global_indicator[i]+'History'] = []
	# raw_data = model.query(INDICATOR, 'CHN')
	# print(data_detail)
	# for i in range(1990,2017):
	# 	year = str(i)
	# 	for j in raw_data[year]:
	# 		da = {'year':year,'value':raw_data[year][j]}
	# 		key = global_indicator[j] + 'History'
	# 		data_detail[key].append(da)
	# print(data_detail)
	db_client.close()