# this file contains functions dealing from download to parse to import
# to the database.
# the flask server api should be in main.py
# scroll down to the bottom to see the example usage

import urllib.request
import csv
import copy
import json
from collections import defaultdict
from mongoengine import connect,StringField, Document
from server_config import *

######################### data process function #########################
def csv_to_list(path):
    # convert csv file to a list
    try:
        with open(path, 'r') as csv_file:
            csv_data = csv.reader(csv_file)
            csv_list = list(csv_data)
    except FileNotFoundError:
        if DEBUG_MODE:
            print(path, 'not found')
        return []
    return csv_list


def wb_csv_parse(indicator, title_row=4, data_col=4, code_col=1):
    # Description:
    #   parse csv file from world bank
    #
    # Input:
    #   indicator
    #   title_row: the row number of the title
    #   data_col: the column number of the data begins
    #   code_col: the column number of the country code
    #
    # Output:
    #   return_dict = {
    #     code 1: {
    #         year 1: data 1,
    #         year 2: data 2
    #     },
    #     code 2: {
    #         year 1: data 1,
    #         year 2: data 2
    #     }
    #   }

    return_dict = defaultdict(str)
    code_dict = defaultdict(str)
    # read the csv file
    csv_list = csv_to_list(CSV_PATH + indicator + '.csv')
    if not csv_list:
        return return_dict
    year_list = csv_list[title_row][data_col:-1]
    time_span = len(year_list)

    # if DEBUG_MODE:
    #     print("\n###",indicator, indicator_to_description[indicator])
    #     print("year list = ", year_list)
    #     print("time span = ", time_span)

    # genereate the return dictionary
    for row in csv_list[title_row + 1:]:
        # generate the code_dict inside return dictionary
        code_dict.clear()
        for i in range(time_span):
            if row[data_col + i]:
                # add key only if the data exists in that year
                year = year_list[i]
                code_dict[year] = row[data_col + i]
        # add code_dict to return_dict only if it is not empty
        if code_dict:
            code = row[code_col]
            return_dict[code] = copy.deepcopy(code_dict)
        # if DEBUG_MODE:
        #     print(row[code_col], code_dict)
    return return_dict


def get_code_dict(code, all_in_one_dict):
    # Description:
    #   convert dictionary
    # Input:
    #   all_in_one_dict = {
    #     indicator 1: {
    #       code 1: {
    #           year 1: data 1,
    #       },
    #     indicator 2: {
    #       code 1: {
    #           year 1: data 1,
    #       }
    #     }
    #   }
    #
    # Output:
    #   return_dict = {
    #     year 1: {
    #         indicator 1: data 1,
    #         indicator 2: data 2
    #     },
    #     year 2: {
    #         indicator 1: data 1,
    #         indicator 2: data 2
    #     }
    #   }
    global indicator_to_description
    return_dict = defaultdict(str)
    year_dict = defaultdict(str)
    # genereate the return dictionary
    for year in range(MIN_YEAR, MAX_YEAR + 1):
        year = str(year)
        # generate the year_dict inside return dictionary
        year_dict.clear()
        for indicator in indicator_to_description.keys():
            # if (DEBUG_MODE):
            #    print("indicator = ", indicator)
            #    print("code = ", code)
            #    print("year = ", year)
            #    print(all_in_one_dict[indicator][code])
            # we need to handle situation when there is no data for a code
            if all_in_one_dict[indicator][code]:
                data = all_in_one_dict[indicator][code][year]
            else:
                data = False
            # add to year_dict only if it is not empty
            if data:
                year_dict[indicator] = data
        # add to return_dict only if it is not empty
        if year_dict:
            return_dict[year] = copy.deepcopy(year_dict)
    return return_dict


############################# mongodb function ##########################
class Country(Document):
    code = StringField(required=True, primary_key=True)
    data = StringField(required=True)

    def __init__(self, code, data, *args, **values):
        super().__init__(*args, **values)
        self.code = code
        self.data = data


def update_country(code, data_dict):
    # Input:
    #   a str code and a default dictionary
    # Description:
    # create or update it to database

    data_json = json.dumps(data_dict)
    instance = Country(code, data_json)
    # if DEBUG_MODE:
    #     print("code = ", instance.code)
    #     print("data = ", instance.data)
    instance.save()


def query_country(code):
    # Input:
    #   a string country code
    # Return:
    #   a default dictionary, could be empty
    
    if not Country.objects(code=code):
        # nothing found in database
        return defaultdict(str)
    data_json =  Country.objects(code=code)[0].data
    data_dict = defaultdict(str, json.loads(data_json))
    return data_dict



########################## initialization function ######################
def init_query_dict():
    # this function will return 3 dictionary
    #   - code_to_country
    #   - country_to_code
    #   - indicator_to_description

    code_to_country = defaultdict(str)
    country_to_code = defaultdict(str)
    csv_list = csv_to_list(CODE_PATH)
    for row in csv_list:
        code_to_country[row[1]] = row[0]
        country_to_code[row[0]] = row[1]
    # generate indicator_to_description
    with open(INDICATOR_PATH, 'r') as json_file:
        indicator_to_description = defaultdict(str, json.load(json_file))
    return code_to_country, country_to_code, indicator_to_description


def init_data_import():
    # import data to database
    # return False if something goes wrong

    global code_to_country
    global indicator_to_description
    # parse csv file and generate a dictionary
    all_in_one_dict = defaultdict(str)
    for indicator in indicator_to_description.keys():
        indicator_dict = wb_csv_parse(indicator)
        all_in_one_dict[indicator] = indicator_dict

    # import data to database by code
    db_client = connect(host=DB_URL)
    for code in code_to_country.keys():
        if DEBUG_MODE:
            print("importing", code, "...")
        data_dict = get_code_dict(code, all_in_one_dict)
        update_country(code, data_dict)
    db_client.close()
    return True


############################# test function #############################
if __name__ == "__main__":
    # generate the global dictionary, which may be useful in main.py
    code_to_country, \
    country_to_code, \
    indicator_to_description = init_query_dict()
    # import data to database, also you can use it to update database
    # init_data_import()
    # query database
    db_client = connect(host=DB_URL)
    print(query_country('USA'))
    db_client.close()