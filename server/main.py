import model
from mongoengine import connect
from collections import defaultdict
from server_config import *
import numpy as np
from normalize_dict_to_array import *
if __name__ == "__main__":
	DB_URL = "mongodb://junipy:comp9321@ds014658.mlab.com:14658/junipy_deploy"
	db_client = connect(host=DB_URL)
	code_to_country, \
	country_to_code, \
	indicator_to_description = model.init_query_dict()

	index_key_list=list(indicator_to_description.keys())

<<<<<<< HEAD
	analysis=Analysis(code_to_country,index_key_list,DB_URL,2000,50)
=======
    # db_client = connect(host=DB_URL)
    # print(model.query_country('USA')['1999'])
>>>>>>> upstream/master

	taken_country_list,\
	taken_data=analysis.select_top_k_country()
	
	country_index_d=analysis.select_non_null(taken_country_list,taken_data)