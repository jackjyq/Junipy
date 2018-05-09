import model
from mongoengine import connect
from server_config import *

if __name__ == "__main__":
    code_to_country, \
    country_to_code, \
    indicator_to_description = model.init_query_dict()

    print(code_to_country.keys())


    # db_client = connect(host=DB_URL)
    # print(model.query_country('USA')['1988'])

    # db_client.close()