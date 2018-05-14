import numpy as np
from collections import defaultdict
import model
from server_config import *
from mongoengine import connect
import pymongo
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Analysis():
	def __init__(self,st_year=2000,k=200,save_file="heatmap.png"):
		self.to_k=k
		self.min_year=st_year
		client = pymongo.MongoClient("mongodb://junipy:comp9321@ds143907.mlab.com:43907/junipy_deploy")
		collection = client.junipy_deploy['collection_indicator']
		self.data_dict={ i["_id"]:i["data"] for i in collection.find()}
		self.country_code=list(self.data_dict.keys())
		self.index_list= list(global_indicators.keys())
		self.select_top_k_country()
		combine_array=np.concatenate(self.taken_data,axis=0)
		self.combine_df=pd.DataFrame(combine_array,columns=self.index_list)
		self.get_corr()
		
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
		for code in self.country_code:
			data_dict_index_year=self.check_index_size(code)
			all_data_dict[code]=self.tran_dict_array(data_dict_index_year)
			for ind,index in enumerate(self.index_list):
				n_array[c_index,ind]=len(data_dict_index_year[index])
			c_index+=1
			country_list.append(code)
		sum_array=np.sum(n_array,axis=1)
		arg_index=np.argsort(sum_array)
		self.select_country=[country_list[i] for i in arg_index[-self.to_k:]]
		self.taken_data=[all_data_dict[code] for code in self.select_country]

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
		sns.heatmap(corr_df.abs(), cmap="Blues", annot=corr_df,
			fmt=".2f", linewidths=.5,square=True,
            yticklabels=corr_df.columns.values)
		plt.title("Global Feature Correlation")
		plt.savefig(file)

	def get_one_trend(self,code):
		index=self.select_country.index(code)
		return self.taken_data[index]

	def plot_one(self,code,indicator,file="trend.png"):
		data_array=self.get_one_trend(code)
		index_indicator=self.index_list.index(indicator)
		select_data=data_array[:,index_indicator]
		data_list=[ [k+self.min_year,i] for k,i in enumerate(select_data) if i>0]
		new_data_array=np.array(data_list)
		plt.figure()
		plt.plot(new_data_array[:,0],new_data_array[:,1])
		plt.title(global_codes[code]["name"]+" "+indicator)
		plt.savefig(file)

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

if __name__ == "__main__":
	analysis=Analysis()
	analysis.get_corr_heatmap("heatmap.png")
	analysis.plot_one("USA","GDP_total")
	#analysis.plots("USA",["GDP_total","GDP_agriculture","GDP_industry","GDP_service"])
