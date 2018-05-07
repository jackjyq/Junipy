import urllib.request
import csv
import copy
from collections import defaultdict
from server_config import *

########################### worldbank function ##########################
def csv_to_list(indicator):
    # convert csv file to a list
    path = CSV_PATH + indicator
    with open(path, 'r') as csv_file:
        csv_data = csv.reader(csv_file)
        csv_list = list(csv_data)
    return csv_list


def get_GDP():
    # https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?view=chart
    # data structure of the return dictionary
    # return_dict: {
    #   code 1: {
    #       year 1: data 1,
    #       year 2: data 2
    #   },
    #   code 2: {
    #       year 1: data 1,
    #       year 2: data 2
    #   }
    # }
    title_row_number = 4    # the row number of the title
    data_col_number = 4     # the column number of the data begins
    code_col_number = 1  # the column number of the country code

    # read the csv file
    csv_list = csv_to_list('API_NY.GDP.MKTP.CD_DS2_en_csv_v2.csv')
    year_list = csv_list[title_row_number][data_col_number]
    time_span = len(year_list)

    if DEBUG_MODE:
        print("year list = ", year_list)
        print("time span = ", time_span)

    # genereate the indicator dictionary
    return_dict = defaultdict(str)
    code_dict = defaultdict(str)
    for row in csv_list[title_row_number + 1:]:
        # generate the code_dict inside indicator dictionary
        code_dict.clear()
        for i in range(time_span):
            if row[data_col_number + i]:
                # add key only if the data exists in that year
                year = year_list[i]
                code_dict[year] = row[data_col_number + i]
        # add code_dict to return_dict only if it is not empty
        if len(code_dict):
            code = row[code_col_number]
            return_dict[code] = copy.deepcopy(code_dict)

    return return_dict



############################# main function #############################
if __name__ == "__main__":
    print(global_wb_data_source['NV.AGR.TOTL.ZS'])