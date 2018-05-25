import model
from mongoengine import connect
from collections import defaultdict
from server_config import *
from flask import Flask,jsonify,Response,send_file
import json
import math
from server_analysis import *

global_indicator = {"GDP_total": "GDP",
                    "GDP_agriculture": "agriculture",
                    "GDP_industry": "industry",
                    "GDP_service": "service",
                    "CO2_emission": "CO2",
                    "PM25_index": "PM25Index",
                    "freshwater_withdrawals": "freshwaterWithdrawals",
                    "Population": "population"
                    }

dataunit = { '3' : 'thousnd',
			 '6' : 'millon',
			 '9' : 'billon',
			 '12' : 'trillion',
			 '15' : 'quadrillion',
			 '18' : 'quintillion',
			 '21' : 'sextillion',
			 '24' : 'septillion',
			 '27' : 'octilion',
			 '30' : 'nonillion',
			 '33' : 'decillion'
}


region_dic = {'Asia': [] ,
			  'Europe': [] ,
			  'Africa': [] ,
			  'Oceania': [] ,
			  'Americas': [] ,
			  'Antarctica': [] ,

	}

country_change_code = {}
for i in global_codes:
	shorts = global_codes[i]['iso2']	
	country_change_code[shorts] = i
	region_dic[global_codes[i]['region']].append(global_codes[i]['iso2']) 

def loadCountryFlags():
 with open('./static/country_flags.json') as json_data:	 
	
   return json.load(json_data)

def sorted_GDP(data_dict):
	data_remove = data_dict.copy()
	for i in data_dict:
		if data_dict[i] == None:
			data_dict[i] = 0
			data_remove.pop(i)
		else:
			shorts = global_codes[i]["iso2"]
			data_remove[shorts] = data_remove.pop(i)
			data_remove[shorts] = float(data_dict[i])
	data_sort = sorted(data_remove.items(), key=lambda d:d[1],reverse = True)
	rank = []
	for i in range(len(data_sort)):
		rank.append(data_sort[i][0])

	return rank

app = Flask(__name__)

@app.route('/allData/<code>', methods=['GET'])
def get_all_data(code):
	alldata = model.query(INDICATOR, code)
	nullformat = {}
	nullformat['year'] = None
	datanull = {}
	for l in global_indicator:
		datanull[global_indicator[l]] = None
	nullformat['data'] = datanull
	select = {}
	#print(alldata)
	for j in range (2016,1990,-1):
		hasdata = 1
		rightkey = {}
		for k in global_indicator:
			if alldata[str(j)][k] == None:
				hasdata = 0
			else:
				rightkey[global_indicator[k]] = alldata[str(j)][k]
		if hasdata == 1:
			select['year'] = j
			select['data'] = rightkey
			break
	if not hasdata:
		select = nullformat
	a  = json.dumps(select)
	return a

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
			shorts = global_codes[i]["iso2"]
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
	short_code  = code
	code = country_change_code[code.upper()]
	data_detail = {}

	for ii in region_dic:
		if short_code in region_dic[ii]:
			data_detail['region'] = ii
			reg = ii

	data_GDP = model.query(OVERVIEW, 'lastest_GDP')
	sortedGDP = sorted_GDP(data_GDP)
	data_detail['worldRank'] = sortedGDP.index(short_code) + 1


	regionGDP = []
	for kk in range(len(sortedGDP)):
		if sortedGDP[kk]  in region_dic[reg]:
			regionGDP.append(sortedGDP[kk])
	
	data_detail['regionRank'] = regionGDP.index(short_code) + 1



	data_detail['name'] = global_codes[code]['name']

	data_detail['introduction'] = model.query(INTRODUCTION, code)

	flag_prefix = 'https://www.cia.gov/library//publications/'\
                  + 'the-world-factbook/graphics/flags/large/'
	flag_suffix = '-lgflag.gif'
	short_code = global_codes[code]['short'].lower()
	flag_url = flag_prefix + short_code + flag_suffix
	data_detail['flag'] = flag_url

	raw_data = model.query(INDICATOR, code)
	for n in global_indicator:
		data_detail[global_indicator[n]+'History'] = {}
		data_detail[global_indicator[n]+'History']['data'] = []
		data_detail[global_indicator[n]+'History']['unit'] = None
	for j in range (2016,1990,-1):
		hasdata = 1
		rightkey = {}
		gdp = float(raw_data[str(j)]['GDP_total'])
		for k in global_indicator:

			if k == 'GDP_agriculture' or k == 'GDP_industry' or k == 'GDP_service':
				if raw_data[str(j)][k] == None:
					hasdata = 0
				else:
					rightkey[global_indicator[k]] = raw_data[str(j)][k]
					da = float(raw_data[str(j)][k])
					rightkey[global_indicator[k]+'Num'] = (da * gdp)/100  
			else:
				rightkey[global_indicator[k]] = raw_data[str(j)][k]
		if hasdata == 1:
			year = j
			datahas = rightkey
			break

	data_detail['year'] = year

	for m in datahas:
		data_detail[m] = datahas[m]
	for i in range(1990,2017):
		gdp = float(raw_data[str(i)]['GDP_total'])
		for j in raw_data[str(i)]:
			if j == 'GDP_agriculture' or j == 'GDP_industry' or j == 'GDP_service':
				if not raw_data[str(i)][j] == None:
					da = float(raw_data[str(i)][j])
					va = ( da * gdp)/100
				else:
					va = None
				da = {'year':i,'value':va}
			else:
				da = {'year':i,'value':raw_data[str(i)][j]}
			key = global_indicator[j] + 'History'
			data_detail[key]['data'].append(da)
	#print(data_detail)
	for i in data_detail:
		if 'History' in i:
			allva = []
			for k in range(len(data_detail[i]['data'])):
				if not data_detail[i]['data'][k]['value'] == None:
					notst = float(data_detail[i]['data'][k]['value'])
					allva.append(notst)
			if not len(allva) == 0:
				min_da = (sorted(allva))[0]
				divide = int(min_da)
				a = len(str(divide)) - 1
				b = a % 3
				c = int(a/3)
				#print(c)
				if c!= 0:
					if b <= 1:
						a = c * 3
					else:
						c = c + 1
						a = c * 3
					unit = dataunit[str(a)]
					a = 10 ** a
					data_detail[i]['unit'] = unit
				else:
					data_detail[i]['unit'] = None
					a = 1

			for k in range(len(data_detail[i]['data'])):
				if not len(allva) == 0:
					if not data_detail[i]['data'][k]['value'] == None:
						notst = float(data_detail[i]['data'][k]['value'])
						ll = notst / a
						data_detail[i]['data'][k]['value'] = '%.2f'% ll
				else:
					data_detail[i]['unit'] = None

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
	#print(get_detail('CN'))

	#app.run()
	# data_regin = []
	# analysis= Analysis()
	# regions=analysis.region_dict.keys()
	
	# for region in regions:
	# 	print(region)
	# 	print(analysis.count_max_part(region))
	# print(region_dic)
	# short_code = 'US'
	# data_detail = {}
	# for i in region_dic:
	# 	if short_code in region_dic[i]:
	# 		data_detail['region'] = i
	# print(data_detail)
	# data_detail
	# data_GDP = model.query(OVERVIEW, 'lastest_GDP')
	# sortedGDP = sorted_GDP(data_GDP)
	# data_detail['worldRank'] = sortedGDP.index('US') + 1
	# data_dict = model.query(OVERVIEW, 'lastest_GDP')
	# data_remove = data_dict.copy()
	# for i in data_dict:
	# 	if data_dict[i] == None:
	# 		data_dict[i] = 0
	# 		data_remove.pop(i)
	# 	else:
	# 		shorts = global_codes[i]["short"]
	# 		data_remove[shorts] = data_remove.pop(i)
	# 		data_remove[shorts] = float(data_dict[i])
	# data_sort = sorted(data_remove.items(), key=lambda d:d[1],reverse = True)
	# rank = []
	# for i in range(len(data_sort)):
	# 	rank.append(data_sort[i][0])
	# print(rank)
	db_client.close()