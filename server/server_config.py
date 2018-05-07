
########################## debug mode control ###########################
DEBUG_MODE = True   # debug switch


######################### data base configuration #######################
#   when debuging database related code, use debug DB_URL
#   when using database, use deploy DB_URL
# DB_URL = mongodb://junipy:comp9321@ds217350.mlab.com:17350/junipy_debug"
DB_URL = "mongodb://junipy:comp9321@ds014658.mlab.com:14658/junipy_deploy"


########################## year configuration ###########################
MIN_YEAR = 1960     # the min year we can use
MAX_YEAR = 2018     # the max year we can use


####################### local path configuration ########################
# csv file will be download in this folder
# the csv file in this folder will be ignored when upload to git
CSV_PATH = './csv/'     
INDICATOR_PATH = './data/indicator.json'
CODE_PATH = './data/country_code.csv'