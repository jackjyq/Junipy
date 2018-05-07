import urllib.request   # used for download
from server_config import *

############################ helper function ############################
def download_indicator(indicator):
    # Input:
    #   given an indicator, eg. 'NY.GDP.MKTP.CD'
    # Return:
    #   True if success, false otherwise
    # Description:
    #   download, upzip, rename to CSV_PATH/indicator.csv
    return True


def name_to_code(name):
    code = ''
    # convert a country name to country code, eg.
    # China -> CHN
    # if not found, return ''
    return code


def code_to_name(code):
    name = ''
    # convert a country code to country name, eg.
    # CHN -> China
    # if not found, return ''
    return name


############################# test function #############################
if __name__ == "__main__":
    download_indicator('NY.GDP.MKTP.CD')