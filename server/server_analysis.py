import numpy as np
from collections import defaultdict,OrderedDict
import model
from server_config import *
from mongoengine import connect
import pymongo
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Analysis():
	def __init__(self,st_year=2000,k=200):
		self.to_k=k
		self.min_year=st_year
		self.needed_index_list=["GDP_total","GDP_agriculture","GDP_industry","GDP_service"]
		client = pymongo.MongoClient("mongodb://junipy:comp9321@ds143907.mlab.com:43907/junipy_deploy")
		collection = client.junipy_deploy['collection_indicator']
		self.data_dict={ i["_id"]:i["data"] for i in collection.find()}
		self.ini_dict()
		self.country_code=list(self.data_dict.keys())
		self.index_list= list(global_indicators.keys())
		self.select_top_k_country()
		combine_array=np.concatenate(self.taken_data,axis=0)
		self.combine_df=pd.DataFrame(combine_array,columns=self.index_list+["class"])
		self.get_corr()
		self.region_dict=self.get_region_list()

	def count_max_part(self,region):
		regoin_data_dict=self.get_regoin_last(region)
		regoin_max_dict={1:[],2:[],3:[]}
		for code,data  in regoin_data_dict.items():
			regoin_max_dict[data['maxPart']].append(code)
		n=sum([ len(i) for k, i in regoin_max_dict.items()])
		if n==0:
			res_l={self.needed_index_list[k]:{"count":len(i),"present":0,"codes":i} for k, i in regoin_max_dict.items()}
		else:
			res_l={self.needed_index_list[k]:{"count":len(i),"present":round(float(len(i))/n,3),"codes":i} for k, i in regoin_max_dict.items()}
		return res_l

	def ini_dict(self):
		temp={}
		for k,temp_dict in self.data_dict.items():
			json_acceptable_string = temp_dict.replace("'", "\"")
			temp_dict = json.loads(json_acceptable_string)
			temp[k]=temp_dict
		self.data_reg_dict=temp

	def get_region_list(self):
		region_dict=defaultdict(list)
		for k,i in global_codes.items():
			region=i["region"]
			if region!="Americas":
				region_dict[region].append(k)
			else:
				region_dict[i["subregion"]].append(k)
		return region_dict

	def get_country_last(self,code):
		alldata = self.data_reg_dict[code]
		datanull = { l: None for l in self.needed_index_list}
		nullformat = {'year':None, 'data':datanull}
		select = {}
		for j in range (2016,1990,-1):
			hasdata = 1
			rightkey = {}
			cur_data=alldata[str(j)]
			for k in self.needed_index_list:
				if cur_data[k]:
					rightkey[k] = cur_data[k]
				else:
					hasdata = 0
			if hasdata == 1:
				select['year'] = j
				select['data'] = rightkey
				break
		if  hasdata==0:
			select = nullformat
		return select

	def get_regoin_last(self,region):
		code_list=self.region_dict[region]
		temp_data_dict={}
		for code in code_list:
			data=self.get_country_last(code)
			if data["year"]:
				temp_data_dict[code]={"data":data}
				max_index=self.get_index(data["data"])
				temp_data_dict[code]["maxPart"]=max_index
		return temp_data_dict

	def get_index(self,data_dict):
		data_list=[ data_dict[i] for k,i in enumerate(self.needed_index_list) if k!=0]
		min_v=max(data_list)
		min_index=data_list.index(min_v)
		return min_index+1

	def check_index_size(self,key):
		data_dict_index_year=defaultdict(dict)
		temp_dict=self.data_dict[key]
		json_acceptable_string = temp_dict.replace("'", "\"")
		temp_dict = json.loads(json_acceptable_string)
		for year,index_dict in temp_dict.items():
			for index,value in index_dict.items():
				data_dict_index_year[index][year]=value
		return data_dict_index_year

	def tran_dict_array(self,data_dict):
		n,d=2017-self.min_year,len(self.index_list)
		data_array=np.zeros((n+1,d))
		for index,year_dict in data_dict.items():
			for year,value in year_dict.items():
				if int(year)-self.min_year>0:
					ind=self.index_list.index(index)
					data_array[int(year)-self.min_year,ind]=value
		return data_array

	def select_top_k_country(self):
		n_array=np.zeros((len(self.country_code),len(self.index_list)))
		c_index=0
		country_list=[]
		all_data_dict={}
		last_GDP={}
		for code in self.country_code:
			data_dict_index_year=self.check_index_size(code)
			all_data_dict[code]=self.tran_dict_array(data_dict_index_year)
			max_value=np.max(all_data_dict[code][:,0])
			for ind,index in enumerate(self.index_list):
				n_array[c_index,ind]=len(data_dict_index_year[index])
			c_index+=1
			country_list.append(code)
			last_GDP[code]=max_value
		sum_array=np.sum(n_array,axis=1)
		arg_index=np.argsort(sum_array)
		self.select_country=[country_list[i] for i in arg_index[-self.to_k:]]
		self.taken_gpu=[last_GDP[code] for code in self.select_country]
		sort_index=np.argsort(self.taken_gpu)
		n1,n2=int(len(self.taken_gpu)*0.5),int(len(self.taken_gpu)*0.75)
		cluster_mapping={}
		for k,i in enumerate(sort_index):
			if k<n1:
				cluster_mapping[i]=0
			elif k<n2:
				cluster_mapping[i]=1
			else:
				cluster_mapping[i]=2
		self.mapping=cluster_mapping
		self.all_data=all_data_dict
		ans=[]
		for code in self.select_country:
			data=all_data_dict[code]
			country_index=self.select_country.index(code)
			label=np.zeros((data.shape[0],1))+self.mapping[country_index]
			ans.append(np.concatenate([data,label],axis=1))
		self.taken_data=ans

	def select_non_null(self,taken_country_list,taken_data):
		country_index_d=defaultdict(dict)
		for index,data in enumerate(taken_data):
			for i in range(len(self.index_list)):
				year_d={ year:value for year,value in enumerate(data[:,i]) if value>0}
				n_d=np.zeros((len(year_d),2))
				year_sd_list=sorted(list(year_d.keys()))
				for ind,year in enumerate(year_sd_list):
					value=year_d[year]
					n_d[ind,:]=year+self.min_year,value
				country_index_d[taken_country_list[index]][self.index_list[i]]=n_d
		self.select_country_index=country_index_d

	def remove_none_get_corr(self,x,y,n):
		data_list=[]
		for i in range(n):
			if x[i] and y[i]:
				if  x[i]>0 and y[i]>0: 
					data_list.append((x[i],y[i]))
		data_df=pd.DataFrame(data_list)
		return data_df.corr()[0][1]

	def get_corr(self):
		data=self.combine_df
		data_df=data.drop(data.columns[1:4],axis=1)
		data_df=data.drop(data.columns[-1],axis=1)
		n,d=data_df.shape
		corr_mat=np.ones((d,d))
		NameL=list(data_df.columns)
		for i in range(d):
			for j in range(d):
				if i<j:
					corr_mat[i,j]=self.remove_none_get_corr(data_df[NameL[i]],data_df[NameL[j]],n)
				elif i>j:
					corr_mat[i,j]=corr_mat[j,i]
		self.corr_mat=pd.DataFrame(np.round(corr_mat,2),columns=NameL)

	def get_corr_heatmap(self,file="heatmap.png"):
		corr_df=self.corr_mat
		corr_mat_abs=np.array(corr_df.abs())
		'''
		sns.heatmap(corr_df.abs(), cmap="Blues", annot=corr_df,
			fmt=".2f", linewidths=.5,square=True,
            yticklabels=corr_df.columns.values)
		plt.title("Global Feature Correlation")
		plt.savefig(file)
		'''
		corr_list=corr_mat_abs.tolist()
		res_list=[ [k1,k,v]  for k,i in enumerate(corr_list) for k1,v in enumerate(i)]
		name_list=[ 'GDP', 'CO2', 'PM25', 'freshWaterWithdrawals', 'population']
		return res_list,name_list

	def get_one_trend(self,code):
		index=self.select_country.index(code)
		return self.taken_data[index]

	def plot_one(self,code,indicator,file="trend.png"):
		data_array=self.get_one_trend(code)
		index_indicator=self.index_list.index(indicator)
		select_data=data_array[:,index_indicator]
		data_list=[ [k+self.min_year,i] for k,i in enumerate(select_data) if i>0]
		new_data_array=np.array(data_list)
		'''
		plt.figure()
		plt.plot(new_data_array[:,0],new_data_array[:,1])
		plt.title(global_codes[code]["name"]+" "+indicator)
		plt.savefig(file)'''

	def pairMatrix(self):
		data=self.combine_df.dropna(how="any")
		data=np.array(data)
		sums=np.sum(data[:,:8],axis=1)
		data=data[sums!=0]
		gdp=data[:,0].tolist()
		min_v=np.min(gdp)
		value=np.floor(np.log(min_v)/np.log(10))
		gdp_2=[ float(i)/( 10**value) for i in gdp]
		data[:,0]=np.array(gdp_2)
		data_list=data.tolist()
		self.combine_df.columns=['GDP',"1","2","3", 'CO2', 'PM25', 'freshWaterWithdrawals', 'population','Class']
		def return_list(i):
			return {self.combine_df.columns[k]:v for k,v in enumerate(i) if k==0 or k>3}
		result_d= [ return_list(i) for i in data_list ]
		Feature_name=['GDP', 'CO2', 'PM25', 'freshWaterWithdrawals', 'population','Class']
		data_df=pd.DataFrame(data,columns=['GDP',"1","2","3", 'CO2', 'PM25', 'freshWaterWithdrawals', 'population','Class'])
		'''
		g = sns.PairGrid(data_df, hue="Class")
		g = g.map_diag(plt.hist)
		g = g.map_offdiag(plt.scatter)
		g = g.add_legend()'''
		return result_d,Feature_name

	def plots(self,code,indicators,file="trend.png"):
		plt.figure()
		data_array=self.get_one_trend(code)
		for k,indicator in enumerate(indicators):
			index_indicator=self.index_list.index(indicator)
			select_data=data_array[:,index_indicator]
			data_list=[ [k+self.min_year,i] for k,i in enumerate(select_data) if i>0]
			new_data_array=np.array(data_list)
			plt.plot(new_data_array[:,0],new_data_array[:,1])
		plt.title(global_codes[code]["name"]+" "+" ".join(indicators))
		plt.savefig(file)


def get_heatmap():
	res_list,name_list=analysis.get_corr_heatmap()
	json_dict={"data":res_list,"names":name_list}
	return json.dumps(json_dict)

def get_pairMartix():
	res_list,name_list=analysis.pairMatrix()
	json_dict={"data":res_list,"names":name_list}
	return json.dumps(json_dict)

if __name__ == "__main__":
	analysis=Analysis()
	#get_heatmap()
	#get_pairMartix()
	#input region code
	regions=analysis.region_dict.keys()
	for region in regions:
		print(region)
		result_d=analysis.count_max_part(region)
		print(result_d)