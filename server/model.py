# Name: Model.py
# Author: Jack Jiang (z5129432)
# Date: 2018-05
# Description:
#   this file contains functions for manipulating database
#   if you just want to use these functions insdead of modify them
#   please scroll down and read from ### interface ### section

import urllib.request, urllib.error
from bs4 import BeautifulSoup
import requests
import csv, re
import copy
import json
import zipfile
import os
from collections import defaultdict
from mongoengine import connect,StringField, FileField, Document
from server_config import *


############################ helper function ############################
def debug(*args):
    if DEBUG_MODE:
        print(*args)


def info(*args):
    if not SILENT_MODE:
        print(*args)


def csv_to_list(path):
    # convert csv file to a list
    try:
        with open(path, 'r') as csv_file:
            csv_data = csv.reader(csv_file)
            csv_list = list(csv_data)
    except FileNotFoundError:
        info(path, 'not found')
        return []
    return csv_list


######################### data retrieve function ########################
def download_indicator(indicator):
    # download, unzip and rename
    global global_indicators
    # download to ZIP_PATH
    url = "http://api.worldbank.org/v2/en/indicator/"\
           + global_indicators[indicator]\
           + "?downloadformat=csv"
    zip_file_path = ZIP_PATH + 'download.zip'
    info('downloading ', url)
    zip_file, headers = urllib.request.urlretrieve(url, zip_file_path)
    # unzip to CSV_PATH
    csv_file_name = headers.get('Content-Disposition')[21:-3] + 'csv'
    zip_ref = zipfile.ZipFile(zip_file_path)
    zip_ref.extract(csv_file_name ,CSV_PATH)
    # rename to indicator.csv
    os.rename(CSV_PATH + csv_file_name, CSV_PATH + indicator + '.csv')
    return True


def download_flag(code):
    # download country flag from CIA website to GIF_PATH
    global global_codes
    flag_prefix = 'https://www.cia.gov/library//publications/'\
                  + 'the-world-factbook/graphics/flags/large/'
    flag_suffix = '-lgflag.gif'
    short_code = global_codes[code]['short'].lower()
    flag_url = flag_prefix + short_code + flag_suffix
    gif_file_path = GIF_PATH + 'flag_' + code + '.gif'
    # starting download
    try:
        urllib.request.urlretrieve(flag_url, gif_file_path)
        info(gif_file_path + 'has been downloaded')
    except urllib.error.HTTPError:
        info(gif_file_path + 'does not exist')
        return False
    return True


def download_introduction(code):
    global global_codes
    intro_prefix = 'https://www.cia.gov/library//publications/'\
                    + 'the-world-factbook/geos/'
    intro_suffix = '.html'
    short_code = global_codes[code]['short'].lower()
    intro_url = intro_prefix + short_code + intro_suffix
    try:
        page = urllib.request.urlopen(intro_url).read()
        soup = BeautifulSoup(page, 'html.parser')
        tag = soup.find_all('div', {'class', 'category_data'})[0]
        intro = tag.contents[0]
        info(intro_url, 'has been parsed')
    except urllib.error.HTTPError:
        info(intro_url, 'not found')
        return NON_INTRO
    return intro

######################### data process function ########################
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
    debug("\n###",indicator)
    debug("year list = ", year_list)
    debug("time span = ", time_span)
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


def get_indicator_dict(country, all_in_one_dict):
    # Description:
    #   convert dictionary to fit schema of Collection_indicator
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
            debug("indicator = ", indicator)
            debug("code = ", country)
            debug("year = ", year)
            debug(all_in_one_dict[indicator][country])
            year_dict[indicator] = all_in_one_dict[indicator][country][year]
        # add to return_dict
        return_dict[year] = copy.deepcopy(year_dict)
    return return_dict



def get_latest_GDP_dict(all_in_one_dict):
    # Description:
    #   convert dictionary to fit schema of Collection_overview
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


############################ database function###########################
class Collection_indicator(Document):
    # schema
    #   key = country code
    #   value = {
    #     year 1: {
    #         indicator 1: data 1,
    #         indicator 2: data 2
    #     },
    #     year 2: {
    #         indicator 1: data 1,
    #         indicator 2: data 2
    #     }
    #   }
    country = StringField(required=True, primary_key=True)
    data = StringField(required=True)

    def __init__(self, country, data, *args, **values):
        super().__init__(*args, **values)
        self.country = country
        self.data = data


def update_collection_indicator(country, data_dict):
    # Input:
    #   a country code and its value
    # Description:
    #   update it to database
    data_json = json.dumps(data_dict)
    instance = Collection_indicator(country, data_json)
    instance.save()


class Collection_overview(Document):
    # schema
    #   key = item (eg. 'lastest_GDP')
    #   value = data (a json)
    item = StringField(required=True, primary_key=True)
    data = StringField(required=True)

    def __init__(self, item, data, *args, **values):
        super().__init__(*args, **values)
        self.item = item
        self.data = data


def update_collection_overview(item, data_dict):
    # Input:
    #   a str code and a default dictionary
    # Description:
    # create or update it to database
    data_json = json.dumps(data_dict)
    instance = Collection_overview(item, data_json)
    instance.save()


class Collection_flag(Document):
    # schema
    #   key = country (eg. 'USA')
    #   flag = a path to a picture
    code = StringField(required=True, primary_key=True)
    flag = FileField()


def update_collection_flag(country, flag):
    # Input:
    #   a str code and a path to a picture
    # Description:
    #   upload flag to database
    instance = Collection_flag(code=country)
    with open(flag, 'rb') as flag_image:
        instance.flag.put(flag_image, content_type = 'image/jpeg')
    instance.save()


class Collection_introduction(Document):
    code = StringField(required=True, primary_key=True)
    intro = StringField(required=True)

    def __init__(self, code, intro, *args, **values):
        super().__init__(*args, **values)
        self.code = code
        self.intro = intro


def update_collection_introduction(code, intro):
    instance = Collection_introduction(code, intro)
    instance.save()

############################### interface ###############################
def init( rebuild_overview=True,
          rebuild_indicator=True,
          rebuild_flag=True,
          rebuild_introduction=True,
          deep_rebuild=False
        ):
    # Description:
    # retrieve data from data source, and update the database
    # once the data base has been setup, you don't need to run it again
    #
    # Arguments:
    # deep_rebuild:
    #   drop collection before update them
    #   this flag will only apply on collections which need to be rebuild
    #   normally, you don't need to do that before update
    global global_codes
    global global_years
    global global_indicators
    # connect to database
    db_client = connect(host=DB_URL)    

    # dowload and preprocess indicator
    if (rebuild_overview or rebuild_indicator):
        for indicator in global_indicators.keys():
            download_indicator(indicator)
    # parse and merge indicator dictionary
    all_in_one_dict = get_all_in_one_dict()

    # overview
    if rebuild_overview:
        if deep_rebuild:
            info("purge overview collection")
            Collection_overview.drop_collection()
        lastest_GDP = get_latest_GDP_dict(all_in_one_dict)
        info("importing lastest_GDP to Collection_overview...")
        update_collection_overview('lastest_GDP', lastest_GDP)
    
    # indicator
    if rebuild_indicator:
        if deep_rebuild:
            info("purge indicator collection")
            Collection_indicator.drop_collection()
        for code in global_codes.keys():
            info("importing ", code, " to Collection_indicator...")
            data_dict = get_indicator_dict(code, all_in_one_dict)
            update_collection_indicator(code, data_dict)

    # flag
    if rebuild_flag:
        if deep_rebuild:
            info("purge indicator flag")
            Collection_flag.drop_collection()

        flag_list = []
        for code in global_codes.keys():
            if download_flag(code):
                flag_list.append(code)
        print('flag_list =\n', flag_list)

        for code in global_codes.keys():
            flag_file = GIF_PATH + 'flag_' + code + '.gif'
            if not os.path.isfile(flag_file):
                # use default flag file
                flag_file = NON_FLAG
            # start uploading
            info('uploading ', flag_file, 'to collection...')
            update_collection_flag(code, flag_file)

    # introduction
    if rebuild_introduction:
        if deep_rebuild:
            info("purge indicator introduction")
            Collection_introduction.drop_collection()
        intro_list = []
        for code in global_codes.keys():
            intro = download_introduction(code)
            if intro != NON_INTRO:
                intro_list.append(code)
            update_collection_introduction(code, intro)
        print('intro_list =\n', intro_list)
    # disconnect to database
    db_client.close()
    info('database has been updated')
    return True



def query(col, doc=None):
    # Input:
    #   col: a collection name defined in server_config.py
    #   doc: the name of the document
    # Return:
    #   if nothing can be found, always return False
    #   otherwise, return suitable data format

    if col == OVERVIEW:
        # Input:
        #   doc is a string of an item, eg. 'lastest_GDP'
        # Return:
        #   a dictionary contains the lastest GDP of all countries
        #   {
        #         country 1: GDP 1,
        #         country 2: GDP 2
        #   }
        #
        if Collection_overview.objects(item=doc):
            data_json =  Collection_overview.objects(item=doc)[0].data
            data_dict = dict(json.loads(data_json))
            return data_dict

    elif col == INDICATOR:
        # Input:
        #   doc is the country code, eg. 'USA'
        # Return:
        #   a dictionary contains indicator of the specified country
        #     {
        #     year 1: {
        #         indicator 1: data 1,
        #         indicator 2: data 2
        #     },
        #     year 2: {
        #         indicator 1: data 1,
        #         indicator 2: data 2
        #     }
        #   }
        #
        if doc:
            if Collection_indicator.objects(country=doc):
                data_json =  Collection_indicator.objects(country=doc)[0].data
                data_dict = dict(json.loads(data_json))
                return data_dict
        else:
            all_data_dict = dict()
            for data_json in Collection_indicator.objects():
                data_dict = dict(json.loads(data_json.data))
                all_data_dict[data_json.country] = data_dict
            return(all_data_dict)

    elif col == FLAG:
        # Input:
        #   doc is the country code, eg. 'USA'
        # Return:
        #   a file object
        #
        instance = Collection_flag.objects(code=doc).first()
        flag_image = instance.flag.read()
        return flag_image

    elif col == INTRODUCTION:
        # Input:
        #   doc is the country code, eg. 'USA'
        # Return:
        #   a file object
        #
        if Collection_introduction.objects(code=doc):
            intro =  Collection_introduction.objects(code=doc)[0].intro
            return intro

    else:   # invalid collection name
        info(col, " is not a valid collection")
    return False




############################# example usage  ############################
if __name__ == "__main__":
    # init(rebuild_overview=True,
    #      rebuild_indicator=True,
    #      rebuild_flag=True,
    #      rebuild_introduction=True,
    #      deep_rebuild=False
    # )    

    db_client = connect(host=DB_URL)

    # print(query(OVERVIEW, 'lastest_GDP'))
    # print(query(INDICATOR, 'USA')['1990'])
    # print(query(INDICATOR)['USA']['1990'])
    # print(query(FLAG, 'ZWE'))
    # print(query(INTRODUCTION, 'CHN'))


    db_client.close()