# this file contains functions dealing from download to parse to import
# to the database.
# scroll down to the bottom to see the example usage

import urllib.request, urllib.error
import requests
import csv
import copy
import json
import zipfile
import os
from collections import defaultdict
from mongoengine import connect,StringField, Document
from server_config import *

######################### data process function #########################
def preprocess(indicator):
    # download, unzip and rename
    global global_indicators
    # download to ZIP_PATH
    url = "http://api.worldbank.org/v2/en/indicator/"\
           + global_indicators[indicator]\
           + "?downloadformat=csv"
    zip_file_path = ZIP_PATH + 'download.zip'
    if DEBUG_MODE:
        print('downloading ', url)
    zip_file, headers = urllib.request.urlretrieve(url, zip_file_path)
    # unzip to CSV_PATH
    csv_file_name = headers.get('Content-Disposition')[21:-3] + 'csv'
    # if DEBUG_MODE:
    #     print('unzipping ', csv_file_name)
    zip_ref = zipfile.ZipFile(zip_file_path)
    zip_ref.extract(csv_file_name ,CSV_PATH)
    # rename to indicator.csv
    os.rename(CSV_PATH + csv_file_name, CSV_PATH + indicator + '.csv')
    return True



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
    #   parse csv file from world bank, and convert it to a dictionary
    #   this function will parse all the exist value, NOT only the
    #   the domain which is defined in server_config.py
    #
    # Input:
    #   indicator
    #   title_row: the row number of the title
    #   data_col: the column number of the data begins
    #   code_col: the column number of the country code
    #
    # Output:
    #   return_dict = {
    #     country code 1: {
    #         year 1: data 1,
    #         year 2: data 2
    #     },
    #     country code 2: {
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
    #     print("\n###",indicator)
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


def filter_dict(input_dict):
    # filter a dictionary returned by wb_csv_parse
    # based on  global_years and global_codes
    # all missing value will be filled by None
    # Input(default dict) & Output(dict):
    #    {
    #     country code 1: {
    #         year 1: data 1,
    #         year 2: data 2
    #     },
    #     country code 2: {
    #         year 1: data 1,
    #         year 2: data 2
    #     }
    #   }
    # 
    global global_codes
    global global_years

    return_dict = dict()
    code_dict = dict()

    for code in global_codes.keys():
        code_dict.clear()
        # generate code dictionary
        if input_dict[code]:
            for year in global_years:
                if input_dict[code][year]:
                    code_dict[year] = input_dict[code][year]
                else:
                    # fill None to the year that does not exist
                    code_dict[year] = None
        else:
            # fill None to every year when code does not exist
            for year in global_years:
                code_dict[year] = None
        return_dict[code] = copy.deepcopy(code_dict)
    return return_dict


############################# country database ##########################
# schema
# country -> years -> indicator

class Junipy_country(Document):
    country = StringField(required=True, primary_key=True)
    data = StringField(required=True)

    def __init__(self, country, data, *args, **values):
        super().__init__(*args, **values)
        self.country = country
        self.data = data


def update_junipy_country(country, data_dict):
    # Input:
    #   a str code and a default dictionary
    # Description:
    # create or update it to database
    data_json = json.dumps(data_dict)
    instance = Junipy_country(country, data_json)
    # if DEBUG_MODE:
    #     print("code = ", instance.code)
    #     print("data = ", instance.data)
    instance.save()


def query_junipy_country(country):
    # Input:
    #   a string country code
    # Return:
    #   a dictionary
    if not Junipy_country.objects(country=country):
        # nothing found in database
        return dict()
    data_json =  Junipy_country.objects(country=country)[0].data
    data_dict = dict(json.loads(data_json))
    return data_dict


def get_all_in_one_dict():
    # merge dictrionary 
    # Return:
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
    global global_codes
    global global_years
    global global_indicators

    all_in_one_dict = dict()
    indicator_dict = dict()
    for indicator in global_indicators.keys():
        # parse all csv files, get a default dictionary
        indicator_dict = filter_dict(wb_csv_parse(indicator))
        all_in_one_dict[indicator] = copy.deepcopy(indicator_dict)
    return all_in_one_dict


def get_country_dict(country, all_in_one_dict):
    # Description:
    #   convert dictionary to fit schema of Junipy_country
    # Input:
    #   all_in_one_dict = {
    #     indicator 1: {
    #       country 1: {
    #           year 1: data 1,
    #       },
    #     indicator 2: {
    #       country 1: {
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
    global global_indicators
    global global_years
    return_dict = dict()
    year_dict = dict()
    # genereate the return dictionary
    for year in global_years:
        # generate the year_dict inside return dictionary
        year_dict.clear()
        for indicator in global_indicators.keys():
            # if (DEBUG_MODE):
            #    print("indicator = ", indicator)
            #    print("code = ", code)
            #    print("year = ", year)
            #    print(all_in_one_dict[indicator][code])
            year_dict[indicator] = all_in_one_dict[indicator][country][year]
        # add to return_dict
        return_dict[year] = copy.deepcopy(year_dict)
    return return_dict

############################ overview database ##########################

class Junipy_overview(Document):
    # country -> years -> indicator
    item = StringField(required=True, primary_key=True)
    data = StringField(required=True)

    def __init__(self, item, data, *args, **values):
        super().__init__(*args, **values)
        self.item = item
        self.data = data


def update_junipy_overview(item, data_dict):
    # Input:
    #   a str code and a default dictionary
    # Description:
    # create or update it to database
    data_json = json.dumps(data_dict)
    instance = Junipy_overview(item, data_json)
    # if DEBUG_MODE:
    #     print("code = ", instance.code)
    #     print("data = ", instance.data)
    instance.save()


def query_junipy_overview(item):
    # Input:
    #   a string country code
    # Return:
    #   a dictionary
    if not Junipy_overview.objects(item=item):
        # nothing found in database
        return dict()
    data_json =  Junipy_overview.objects(item=item)[0].data
    data_dict = dict(json.loads(data_json))
    return data_dict


def get_latest_GDP_dict(all_in_one_dict):
    # Description:
    #   convert dictionary to fit schema of Junipy_overview
    # Input:
    #   all_in_one_dict = {
    #     indicator 1: {
    #       country 1: {
    #           year 1: data 1,
    #       },
    #     indicator 2: {
    #       country 1: {
    #           year 1: data 1,
    #       }
    #     }
    #   }
    #
    # Output:
    #   return_dict = {
    #         country 1: GDP 1,
    #         country 2: GDP 2
    #   }

    global global_years
    global global_codes
    return_dict = dict()
    gdp_dict = all_in_one_dict["GDP_total"]
    latest_year = global_years[-1]
    for code in global_codes.keys():
        return_dict[code] = gdp_dict[code][latest_year]
    return return_dict



########################## initialization function ######################
def reset_database():
    # create or update database
    global global_codes
    global global_years
    global global_indicators

    # preprocess data source
    for indicator in global_indicators.keys():
        preprocess(indicator)

    # parse and merge dictionary
    all_in_one_dict = get_all_in_one_dict()


    db_client = connect(host=DB_URL)
    # import data to Junipy_overview
    lastest_GDP = get_latest_GDP_dict(all_in_one_dict)
    
    if DEBUG_MODE:
        print("importing lastest_GDP to Junipy_overview...")
    # Junipy_overview.drop_collection()
    update_junipy_overview('lastest_GDP', lastest_GDP)

    # import data to Junipy_country
    # Junipy_country.drop_collection()
    for code in global_codes.keys():
        if DEBUG_MODE:
            print("importing ", code, " to Junipy_country...")
        data_dict = get_country_dict(code, all_in_one_dict)
        update_junipy_country(code, data_dict)

    db_client.close()
    return True


# has not implemented yet
def get_flag_from_CIA(reset=False):
    # download country flag from CIA website to GIF_PATH
    # Input:
    #   True: download gif files (may take long time)
    #   False: generate dictionary from local cache
    #
    # return 
    # a dictionary: flag[code] = local gif path
    # if flag does not exist, set path to NON_FLAG
    global global_codes
    flag = dict()
    flag_prefix = \
        'https://www.cia.gov/library//publications/the-world-factbook/graphics/flags/large/'
    flag_suffix = '-lgflag.gif'

    # generate the dictionary contains url
    for code in global_codes.keys():
        short = global_codes[code]['short'].lower()
        flag_url = flag_prefix + short + flag_suffix
        gif_file_path = GIF_PATH + code + '.gif'
        try:
            gif_file, headers = urllib.request.urlretrieve(flag_url, gif_file_path)
            if DEBUG_MODE:
                print(gif_file_path + 'has been downloaded')
                flag[code] = gif_file_path
        except urllib.error.HTTPError:
            if DEBUG_MODE:
                print(gif_file_path + 'does not exist')
            flag[code] = NON_FLAG

    print(flag)
############################# test function #############################
if __name__ == "__main__":
    # download and import the database
    # once the data base has been setup, you don't need to run it again
    # only used when change database
    # reset_database()

    # db_client = connect(host=DB_URL)
    # # query overview database
    # print(query_junipy_overview('lastest_GDP'))

    # # query country database
    # print(query_junipy_country('USA')['1990'])
    # db_client.close()

    # get a dictionary of country flag and locator
    get_flag_from_CIA()
