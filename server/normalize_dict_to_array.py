import numpy as np
from collections import defaultdict
import model
from mongoengine import connect
class Analysis():
	def __init__(self,code_to_country,index_key_list,DB_URL,st_year=2000,k=50):
		self.index_key_list=index_key_list
		self.code_to_country=code_to_country
		self.to_k=k
		self.min_year=st_year
		self.DB_URL=DB_URL

	def check_index_size(self,key):
		db_client = connect(host=self.DB_URL)
		data_dict=model.query_country(key)
		data_dict_index_year=defaultdict(dict)
		for year,index_dict in data_dict.items():
			for index,value in index_dict.items():
				data_dict_index_year[index][year]=value
		return data_dict_index_year

	def tran_dict_array(self,data_dict):
		n,d=2017-self.min_year,len(self.index_key_list)
		data_array=np.zeros((n+1,d))
		for index,year_dict in data_dict.items():
			for year,value in year_dict.items():
				if int(year)-self.min_year>0:
					ind=self.index_key_list.index(index)
					data_array[int(year)-self.min_year,ind]=value
		return data_array

	def select_top_k_country(self):
		n_array=np.zeros((len(self.code_to_country),len(self.index_key_list)))
		c_index=0
		country_list=[]
		all_data_dict={}
		for code in self.code_to_country:
			data_dict_index_year=self.check_index_size(code)
			data_array=self.tran_dict_array(data_dict_index_year,self.min_year)
			all_data_dict[code]=data_array
			for ind,index in enumerate(self.index_key_list):
				try:
					n_array[c_index,ind]=len(data_dict_index_year[index])
				except KeyError:
					pass
			c_index+=1
			country_list.append(code)
		sum_array=np.sum(n_array,axis=1)
		arg_index=np.argsort(sum_array)
		taken_country_list=[country_list[i] for i in arg_index[-self.to_k:]]
		taken_data=[all_data_dict[code] for code in taken_country_list]
		self.select_country=taken_country_list
		return taken_country_list,taken_data

	def select_non_null(self,taken_country_list,taken_data):
		country_index_d=defaultdict(dict)
		for index,data in enumerate(taken_data):
			for i in range(len(self.index_key_list)):
				year_d={ year:value for year,value in enumerate(data[:,i]) if value>0}
				n_d=np.zeros((len(year_d),2))
				year_sd_list=sorted(list(year_d.keys()))
				for ind,year in enumerate(year_sd_list):
					value=year_d[year]
					n_d[ind,:]=year+self.min_year,value
				country_index_d[taken_country_list[index]][self.index_key_list[i]]=n_d
		self.select_country_index=country_index_d
		return country_index_d