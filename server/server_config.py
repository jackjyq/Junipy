
############################# print control #############################
DEBUG_MODE = False   # True: print as much information False: default
SILENT_MODE = False  # True: print as less information False: default



########################## local configuration ##########################
# files inside tmp folder will be ignored by Git
ZIP_PATH = './tmp/' # zip file will be download here
CSV_PATH = './tmp/' # csv file will be unzip here
GIF_PATH = './tmp/' # gif file will be download here

# cache folder
FLAG_CACHE = './static/'   # used to store retrieved flag image
# LOCATOR_CACHE = './static/'   # used to store retrieved locator image

# default value
NON_FLAG = './static/default_flag.gif'     
# NON_LOCATOR = './static/default_flag.gif'  
NON_INTRO = ''      # default country introduction



########################### mlab configuration ##########################
# database for debug
# DB_URL = "mongodb://junipy:comp9321@ds217350.mlab.com:17350/junipy_debug"
# database for deploy
DB_URL = "mongodb://junipy:comp9321@ds143907.mlab.com:43907/junipy_deploy"

# database collections, used in query(col=database collection)
OVERVIEW = 1    # latest GDP
INDICATOR = 2
FLAG = 3
# LOCATOR = 4
INTRODUCTION = 5    # country introduction



############################ data source domain #########################
# the years to be processed
global_years = [str(year) for year in range(1990, 2016 + 1)]

# the indicators to be processed
global_indicators = {"GDP_total": "NY.GDP.MKTP.CD",
                    "GDP_agriculture": "NV.AGR.TOTL.ZS",
                    "GDP_industry": "NV.IND.TOTL.ZS",
                    "GDP_service": "NV.SRV.TETC.ZS",
                    "CO2_emission": "EN.ATM.CO2E.KT",
                    "PM25_index": "EN.ATM.PM25.MC.M3",
                    "freshwater_withdrawals": "ER.H2O.FWTL.K3",
                    "Population": "SP.POP.TOTL"
                    }

# the country code to be processed
global_codes = {
    "AFG": {
        "name": "Afghanistan",
        "iso2": "AF",
        "short": "AF",
        "region": "Asia",
        "Southern Asia": "Southern Asia"
    },
    "ALB": {
        "name": "Albania",
        "iso2": "AL",
        "short": "AL",
        "region": "Europe",
        "Southern Europe": "Southern Europe"
    },
    "DZA": {
        "name": "Algeria",
        "iso2": "DZ",
        "short": "AG",
        "region": "Africa",
        "Northern Africa": "Northern Africa"
    },
    "ASM": {
        "name": "American Samoa",
        "iso2": "AS",
        "short": "AQ",
        "region": "Oceania",
        "Polynesia": "Polynesia"
    },
    "AND": {
        "name": "Andorra",
        "iso2": "AD",
        "short": "AN",
        "region": "Europe",
        "Southern Europe": "Southern Europe"
    },
    "AGO": {
        "name": "Angola",
        "iso2": "AO",
        "short": "AO",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "AIA": {
        "name": "Anguilla",
        "iso2": "AI",
        "short": "AV",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "ATA": {
        "name": "Antarctica",
        "iso2": "AQ",
        "short": "AY",
        "region": "",
        "": ""
    },
    "ATG": {
        "name": "Antigua and Barbuda",
        "iso2": "AG",
        "short": "AC",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "ARG": {
        "name": "Argentina",
        "iso2": "AR",
        "short": "AR",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "ARM": {
        "name": "Armenia",
        "iso2": "AM",
        "short": "AM",
        "region": "Asia",
        "Western Asia": "Western Asia"
    },
    "ABW": {
        "name": "Aruba",
        "iso2": "AW",
        "short": "AA",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "AUS": {
        "name": "Australia",
        "iso2": "AU",
        "short": "AS",
        "region": "Oceania",
        "Australia and New Zealand": "Australia and New Zealand"
    },
    "AUT": {
        "name": "Austria",
        "iso2": "AT",
        "short": "AU",
        "region": "Europe",
        "Western Europe": "Western Europe"
    },
    "AZE": {
        "name": "Azerbaijan",
        "iso2": "AZ",
        "short": "AJ",
        "region": "Asia",
        "Western Asia": "Western Asia"
    },
    "BHS": {
        "name": "Bahamas",
        "iso2": "BS",
        "short": "BF",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "BHR": {
        "name": "Bahrain",
        "iso2": "BH",
        "short": "BA",
        "region": "Asia",
        "Western Asia": "Western Asia"
    },
    "BGD": {
        "name": "Bangladesh",
        "iso2": "BD",
        "short": "BG",
        "region": "Asia",
        "Southern Asia": "Southern Asia"
    },
    "BRB": {
        "name": "Barbados",
        "iso2": "BB",
        "short": "BB",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "BLR": {
        "name": "Belarus",
        "iso2": "BY",
        "short": "BO",
        "region": "Europe",
        "Eastern Europe": "Eastern Europe"
    },
    "BEL": {
        "name": "Belgium",
        "iso2": "BE",
        "short": "BE",
        "region": "Europe",
        "Western Europe": "Western Europe"
    },
    "BLZ": {
        "name": "Belize",
        "iso2": "BZ",
        "short": "BH",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "BEN": {
        "name": "Benin",
        "iso2": "BJ",
        "short": "BN",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "BMU": {
        "name": "Bermuda",
        "iso2": "BM",
        "short": "BD",
        "region": "Americas",
        "Northern America": "Northern America"
    },
    "BTN": {
        "name": "Bhutan",
        "iso2": "BT",
        "short": "BT",
        "region": "Asia",
        "Southern Asia": "Southern Asia"
    },
    "BOL": {
        "name": "Bolivia (Plurinational State of)",
        "iso2": "BO",
        "short": "BL",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "BES": {
        "name": "Bonaire, Sint Eustatius and Saba",
        "iso2": "BQ",
        "short": "NL",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "BIH": {
        "name": "Bosnia and Herzegovina",
        "iso2": "BA",
        "short": "BK",
        "region": "Europe",
        "Southern Europe": "Southern Europe"
    },
    "BWA": {
        "name": "Botswana",
        "iso2": "BW",
        "short": "BC",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "BVT": {
        "name": "Bouvet Island",
        "iso2": "BV",
        "short": "BV",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "BRA": {
        "name": "Brazil",
        "iso2": "BR",
        "short": "BR",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "IOT": {
        "name": "British Indian Ocean Territory",
        "iso2": "IO",
        "short": "IO",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "VGB": {
        "name": "British Virgin Islands",
        "iso2": "VG",
        "short": "VI",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "BRN": {
        "name": "Brunei Darussalam",
        "iso2": "BN",
        "short": "BX",
        "region": "Asia",
        "South-eastern Asia": "South-eastern Asia"
    },
    "BGR": {
        "name": "Bulgaria",
        "iso2": "BG",
        "short": "BU",
        "region": "Europe",
        "Eastern Europe": "Eastern Europe"
    },
    "BFA": {
        "name": "Burkina Faso",
        "iso2": "BF",
        "short": "UV",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "BDI": {
        "name": "Burundi",
        "iso2": "BI",
        "short": "BY",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "CPV": {
        "name": "Cabo Verde",
        "iso2": "CV",
        "short": "CV",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "KHM": {
        "name": "Cambodia",
        "iso2": "KH",
        "short": "CB",
        "region": "Asia",
        "South-eastern Asia": "South-eastern Asia"
    },
    "CMR": {
        "name": "Cameroon",
        "iso2": "CM",
        "short": "CM",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "CAN": {
        "name": "Canada",
        "iso2": "CA",
        "short": "CA",
        "region": "Americas",
        "Northern America": "Northern America"
    },
    "CYM": {
        "name": "Cayman Islands",
        "iso2": "KY",
        "short": "CJ",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "CAF": {
        "name": "Central African Republic",
        "iso2": "CF",
        "short": "CT",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "TCD": {
        "name": "Chad",
        "iso2": "TD",
        "short": "CD",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "CHL": {
        "name": "Chile",
        "iso2": "CL",
        "short": "CI",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "CHN": {
        "name": "China",
        "iso2": "CN",
        "short": "CH",
        "region": "Asia",
        "Eastern Asia": "Eastern Asia"
    },
    "HKG": {
        "name": "China, Hong Kong Special Administrative Region",
        "iso2": "HK",
        "short": "HK",
        "region": "Asia",
        "Eastern Asia": "Eastern Asia"
    },
    "MAC": {
        "name": "China, Macao Special Administrative Region",
        "iso2": "MO",
        "short": "MC",
        "region": "Asia",
        "Eastern Asia": "Eastern Asia"
    },
    "CXR": {
        "name": "Christmas Island",
        "iso2": "CX",
        "short": "KT",
        "region": "Oceania",
        "Australia and New Zealand": "Australia and New Zealand"
    },
    "CCK": {
        "name": "Cocos (Keeling) Islands",
        "iso2": "CC",
        "short": "CK",
        "region": "Oceania",
        "Australia and New Zealand": "Australia and New Zealand"
    },
    "COL": {
        "name": "Colombia",
        "iso2": "CO",
        "short": "CO",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "COM": {
        "name": "Comoros",
        "iso2": "KM",
        "short": "CN",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "COG": {
        "name": "Congo",
        "iso2": "CG",
        "short": "CF",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "COK": {
        "name": "Cook Islands",
        "iso2": "CK",
        "short": "CW",
        "region": "Oceania",
        "Polynesia": "Polynesia"
    },
    "CRI": {
        "name": "Costa Rica",
        "iso2": "CR",
        "short": "CS",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "HRV": {
        "name": "Croatia",
        "iso2": "HR",
        "short": "HR",
        "region": "Europe",
        "Southern Europe": "Southern Europe"
    },
    "CUB": {
        "name": "Cuba",
        "iso2": "CU",
        "short": "CU",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "CUW": {
        "name": "Cura ao",
        "iso2": "CW",
        "short": "UC",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "CYP": {
        "name": "Cyprus",
        "iso2": "CY",
        "short": "CY",
        "region": "Asia",
        "Western Asia": "Western Asia"
    },
    "CZE": {
        "name": "Czechia",
        "iso2": "CZ",
        "short": "EZ",
        "region": "Europe",
        "Eastern Europe": "Eastern Europe"
    },
    "CIV": {
        "name": "C te d'Ivoire",
        "iso2": "CI",
        "short": "IV",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "PRK": {
        "name": "Democratic People's Republic of Korea",
        "iso2": "KP",
        "short": "KN",
        "region": "Asia",
        "Eastern Asia": "Eastern Asia"
    },
    "COD": {
        "name": "Democratic Republic of the Congo",
        "iso2": "CD",
        "short": "CG",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "DNK": {
        "name": "Denmark",
        "iso2": "DK",
        "short": "DA",
        "region": "Europe",
        "Northern Europe": "Northern Europe"
    },
    "DJI": {
        "name": "Djibouti",
        "iso2": "DJ",
        "short": "DJ",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "DMA": {
        "name": "Dominica",
        "iso2": "DM",
        "short": "DO",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "DOM": {
        "name": "Dominican Republic",
        "iso2": "DO",
        "short": "DR",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "ECU": {
        "name": "Ecuador",
        "iso2": "EC",
        "short": "EC",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "EGY": {
        "name": "Egypt",
        "iso2": "EG",
        "short": "EG",
        "region": "Africa",
        "Northern Africa": "Northern Africa"
    },
    "SLV": {
        "name": "El Salvador",
        "iso2": "SV",
        "short": "ES",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "GNQ": {
        "name": "Equatorial Guinea",
        "iso2": "GQ",
        "short": "EK",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "ERI": {
        "name": "Eritrea",
        "iso2": "ER",
        "short": "ER",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "EST": {
        "name": "Estonia",
        "iso2": "EE",
        "short": "EN",
        "region": "Europe",
        "Northern Europe": "Northern Europe"
    },
    "ETH": {
        "name": "Ethiopia",
        "iso2": "ET",
        "short": "ET",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "FLK": {
        "name": "Falkland Islands (Malvinas)",
        "iso2": "FK",
        "short": "FK",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "FRO": {
        "name": "Faroe Islands",
        "iso2": "FO",
        "short": "FO",
        "region": "Europe",
        "Northern Europe": "Northern Europe"
    },
    "FJI": {
        "name": "Fiji",
        "iso2": "FJ",
        "short": "FJ",
        "region": "Oceania",
        "Melanesia": "Melanesia"
    },
    "FIN": {
        "name": "Finland",
        "iso2": "FI",
        "short": "FI",
        "region": "Europe",
        "Northern Europe": "Northern Europe"
    },
    "FRA": {
        "name": "France",
        "iso2": "FR",
        "short": "FR",
        "region": "Europe",
        "Western Europe": "Western Europe"
    },
    "GUF": {
        "name": "French Guiana",
        "iso2": "GF",
        "short": "FG",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "PYF": {
        "name": "French Polynesia",
        "iso2": "PF",
        "short": "FP",
        "region": "Oceania",
        "Polynesia": "Polynesia"
    },
    "ATF": {
        "name": "French Southern Territories",
        "iso2": "TF",
        "short": "FS",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "GAB": {
        "name": "Gabon",
        "iso2": "GA",
        "short": "GB",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "GMB": {
        "name": "Gambia",
        "iso2": "GM",
        "short": "GA",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "GEO": {
        "name": "Georgia",
        "iso2": "GE",
        "short": "GG",
        "region": "Asia",
        "Western Asia": "Western Asia"
    },
    "DEU": {
        "name": "Germany",
        "iso2": "DE",
        "short": "GM",
        "region": "Europe",
        "Western Europe": "Western Europe"
    },
    "GHA": {
        "name": "Ghana",
        "iso2": "GH",
        "short": "GH",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "GIB": {
        "name": "Gibraltar",
        "iso2": "GI",
        "short": "GI",
        "region": "Europe",
        "Southern Europe": "Southern Europe"
    },
    "GRC": {
        "name": "Greece",
        "iso2": "GR",
        "short": "GR",
        "region": "Europe",
        "Southern Europe": "Southern Europe"
    },
    "GRL": {
        "name": "Greenland",
        "iso2": "GL",
        "short": "GL",
        "region": "Americas",
        "Northern America": "Northern America"
    },
    "GRD": {
        "name": "Grenada",
        "iso2": "GD",
        "short": "GJ",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "GLP": {
        "name": "Guadeloupe",
        "iso2": "GP",
        "short": "GP",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "GUM": {
        "name": "Guam",
        "iso2": "GU",
        "short": "GQ",
        "region": "Oceania",
        "Micronesia": "Micronesia"
    },
    "GTM": {
        "name": "Guatemala",
        "iso2": "GT",
        "short": "GT",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "GGY": {
        "name": "Guernsey",
        "iso2": "GG",
        "short": "GK",
        "region": "Europe",
        "Northern Europe": "Northern Europe"
    },
    "GIN": {
        "name": "Guinea",
        "iso2": "GN",
        "short": "GV",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "GNB": {
        "name": "Guinea-Bissau",
        "iso2": "GW",
        "short": "PU",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "GUY": {
        "name": "Guyana",
        "iso2": "GY",
        "short": "GY",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "HTI": {
        "name": "Haiti",
        "iso2": "HT",
        "short": "HA",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "HMD": {
        "name": "Heard Island and McDonald Islands",
        "iso2": "HM",
        "short": "HM",
        "region": "Oceania",
        "Australia and New Zealand": "Australia and New Zealand"
    },
    "VAT": {
        "name": "Holy See",
        "iso2": "VA",
        "short": "VT",
        "region": "Europe",
        "Southern Europe": "Southern Europe"
    },
    "HND": {
        "name": "Honduras",
        "iso2": "HN",
        "short": "HO",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "HUN": {
        "name": "Hungary",
        "iso2": "HU",
        "short": "HU",
        "region": "Europe",
        "Eastern Europe": "Eastern Europe"
    },
    "ISL": {
        "name": "Iceland",
        "iso2": "IS",
        "short": "IC",
        "region": "Europe",
        "Northern Europe": "Northern Europe"
    },
    "IND": {
        "name": "India",
        "iso2": "IN",
        "short": "IN",
        "region": "Asia",
        "Southern Asia": "Southern Asia"
    },
    "IDN": {
        "name": "Indonesia",
        "iso2": "ID",
        "short": "ID",
        "region": "Asia",
        "South-eastern Asia": "South-eastern Asia"
    },
    "IRN": {
        "name": "Iran (Islamic Republic of)",
        "iso2": "IR",
        "short": "IR",
        "region": "Asia",
        "Southern Asia": "Southern Asia"
    },
    "IRQ": {
        "name": "Iraq",
        "iso2": "IQ",
        "short": "IZ",
        "region": "Asia",
        "Western Asia": "Western Asia"
    },
    "IRL": {
        "name": "Ireland",
        "iso2": "IE",
        "short": "EI",
        "region": "Europe",
        "Northern Europe": "Northern Europe"
    },
    "IMN": {
        "name": "Isle of Man",
        "iso2": "IM",
        "short": "IM",
        "region": "Europe",
        "Northern Europe": "Northern Europe"
    },
    "ISR": {
        "name": "Israel",
        "iso2": "IL",
        "short": "IS",
        "region": "Asia",
        "Western Asia": "Western Asia"
    },
    "ITA": {
        "name": "Italy",
        "iso2": "IT",
        "short": "IT",
        "region": "Europe",
        "Southern Europe": "Southern Europe"
    },
    "JAM": {
        "name": "Jamaica",
        "iso2": "JM",
        "short": "JM",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "JPN": {
        "name": "Japan",
        "iso2": "JP",
        "short": "JA",
        "region": "Asia",
        "Eastern Asia": "Eastern Asia"
    },
    "JEY": {
        "name": "Jersey",
        "iso2": "JE",
        "short": "JE",
        "region": "Europe",
        "Northern Europe": "Northern Europe"
    },
    "JOR": {
        "name": "Jordan",
        "iso2": "JO",
        "short": "JO",
        "region": "Asia",
        "Western Asia": "Western Asia"
    },
    "KAZ": {
        "name": "Kazakhstan",
        "iso2": "KZ",
        "short": "KZ",
        "region": "Asia",
        "Central Asia": "Central Asia"
    },
    "KEN": {
        "name": "Kenya",
        "iso2": "KE",
        "short": "KE",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "KIR": {
        "name": "Kiribati",
        "iso2": "KI",
        "short": "KR",
        "region": "Oceania",
        "Micronesia": "Micronesia"
    },
    "KWT": {
        "name": "Kuwait",
        "iso2": "KW",
        "short": "KU",
        "region": "Asia",
        "Western Asia": "Western Asia"
    },
    "KGZ": {
        "name": "Kyrgyzstan",
        "iso2": "KG",
        "short": "KG",
        "region": "Asia",
        "Central Asia": "Central Asia"
    },
    "LAO": {
        "name": "Lao People's Democratic Republic",
        "iso2": "LA",
        "short": "LA",
        "region": "Asia",
        "South-eastern Asia": "South-eastern Asia"
    },
    "LVA": {
        "name": "Latvia",
        "iso2": "LV",
        "short": "LG",
        "region": "Europe",
        "Northern Europe": "Northern Europe"
    },
    "LBN": {
        "name": "Lebanon",
        "iso2": "LB",
        "short": "LE",
        "region": "Asia",
        "Western Asia": "Western Asia"
    },
    "LSO": {
        "name": "Lesotho",
        "iso2": "LS",
        "short": "LT",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "LBR": {
        "name": "Liberia",
        "iso2": "LR",
        "short": "LI",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "LBY": {
        "name": "Libya",
        "iso2": "LY",
        "short": "LY",
        "region": "Africa",
        "Northern Africa": "Northern Africa"
    },
    "LIE": {
        "name": "Liechtenstein",
        "iso2": "LI",
        "short": "LS",
        "region": "Europe",
        "Western Europe": "Western Europe"
    },
    "LTU": {
        "name": "Lithuania",
        "iso2": "LT",
        "short": "LH",
        "region": "Europe",
        "Northern Europe": "Northern Europe"
    },
    "LUX": {
        "name": "Luxembourg",
        "iso2": "LU",
        "short": "LU",
        "region": "Europe",
        "Western Europe": "Western Europe"
    },
    "MDG": {
        "name": "Madagascar",
        "iso2": "MG",
        "short": "MA",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "MWI": {
        "name": "Malawi",
        "iso2": "MW",
        "short": "MI",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "MYS": {
        "name": "Malaysia",
        "iso2": "MY",
        "short": "MY",
        "region": "Asia",
        "South-eastern Asia": "South-eastern Asia"
    },
    "MDV": {
        "name": "Maldives",
        "iso2": "MV",
        "short": "MV",
        "region": "Asia",
        "Southern Asia": "Southern Asia"
    },
    "MLI": {
        "name": "Mali",
        "iso2": "ML",
        "short": "ML",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "MLT": {
        "name": "Malta",
        "iso2": "MT",
        "short": "MT",
        "region": "Europe",
        "Southern Europe": "Southern Europe"
    },
    "MHL": {
        "name": "Marshall Islands",
        "iso2": "MH",
        "short": "RM",
        "region": "Oceania",
        "Micronesia": "Micronesia"
    },
    "MTQ": {
        "name": "Martinique",
        "iso2": "MQ",
        "short": "MB",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "MRT": {
        "name": "Mauritania",
        "iso2": "MR",
        "short": "MR",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "MUS": {
        "name": "Mauritius",
        "iso2": "MU",
        "short": "MP",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "MYT": {
        "name": "Mayotte",
        "iso2": "YT",
        "short": "MF",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "MEX": {
        "name": "Mexico",
        "iso2": "MX",
        "short": "MX",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "FSM": {
        "name": "Micronesia (Federated States of)",
        "iso2": "FM",
        "short": "FM",
        "region": "Oceania",
        "Micronesia": "Micronesia"
    },
    "MCO": {
        "name": "Monaco",
        "iso2": "MC",
        "short": "MN",
        "region": "Europe",
        "Western Europe": "Western Europe"
    },
    "MNG": {
        "name": "Mongolia",
        "iso2": "MN",
        "short": "MG",
        "region": "Asia",
        "Eastern Asia": "Eastern Asia"
    },
    "MNE": {
        "name": "Montenegro",
        "iso2": "ME",
        "short": "MJ",
        "region": "Europe",
        "Southern Europe": "Southern Europe"
    },
    "MSR": {
        "name": "Montserrat",
        "iso2": "MS",
        "short": "MH",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "MAR": {
        "name": "Morocco",
        "iso2": "MA",
        "short": "MO",
        "region": "Africa",
        "Northern Africa": "Northern Africa"
    },
    "MOZ": {
        "name": "Mozambique",
        "iso2": "MZ",
        "short": "MZ",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "MMR": {
        "name": "Myanmar",
        "iso2": "MM",
        "short": "BM",
        "region": "Asia",
        "South-eastern Asia": "South-eastern Asia"
    },
    "NAM": {
        "name": "Namibia",
        "iso2": "NA",
        "short": "WA",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "NRU": {
        "name": "Nauru",
        "iso2": "NR",
        "short": "NR",
        "region": "Oceania",
        "Micronesia": "Micronesia"
    },
    "NPL": {
        "name": "Nepal",
        "iso2": "NP",
        "short": "NP",
        "region": "Asia",
        "Southern Asia": "Southern Asia"
    },
    "NLD": {
        "name": "Netherlands",
        "iso2": "NL",
        "short": "NL",
        "region": "Europe",
        "Western Europe": "Western Europe"
    },
    "NCL": {
        "name": "New Caledonia",
        "iso2": "NC",
        "short": "NC",
        "region": "Oceania",
        "Melanesia": "Melanesia"
    },
    "NZL": {
        "name": "New Zealand",
        "iso2": "NZ",
        "short": "NZ",
        "region": "Oceania",
        "Australia and New Zealand": "Australia and New Zealand"
    },
    "NIC": {
        "name": "Nicaragua",
        "iso2": "NI",
        "short": "NU",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "NER": {
        "name": "Niger",
        "iso2": "NE",
        "short": "NG",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "NGA": {
        "name": "Nigeria",
        "iso2": "NG",
        "short": "NI",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "NIU": {
        "name": "Niue",
        "iso2": "NU",
        "short": "NE",
        "region": "Oceania",
        "Polynesia": "Polynesia"
    },
    "NFK": {
        "name": "Norfolk Island",
        "iso2": "NF",
        "short": "NF",
        "region": "Oceania",
        "Australia and New Zealand": "Australia and New Zealand"
    },
    "MNP": {
        "name": "Northern Mariana Islands",
        "iso2": "MP",
        "short": "CQ",
        "region": "Oceania",
        "Micronesia": "Micronesia"
    },
    "NOR": {
        "name": "Norway",
        "iso2": "NO",
        "short": "NO",
        "region": "Europe",
        "Northern Europe": "Northern Europe"
    },
    "OMN": {
        "name": "Oman",
        "iso2": "OM",
        "short": "MU",
        "region": "Asia",
        "Western Asia": "Western Asia"
    },
    "PAK": {
        "name": "Pakistan",
        "iso2": "PK",
        "short": "PK",
        "region": "Asia",
        "Southern Asia": "Southern Asia"
    },
    "PLW": {
        "name": "Palau",
        "iso2": "PW",
        "short": "PS",
        "region": "Oceania",
        "Micronesia": "Micronesia"
    },
    "PAN": {
        "name": "Panama",
        "iso2": "PA",
        "short": "PM",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "PNG": {
        "name": "Papua New Guinea",
        "iso2": "PG",
        "short": "PP",
        "region": "Oceania",
        "Melanesia": "Melanesia"
    },
    "PRY": {
        "name": "Paraguay",
        "iso2": "PY",
        "short": "PA",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "PER": {
        "name": "Peru",
        "iso2": "PE",
        "short": "PE",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "PHL": {
        "name": "Philippines",
        "iso2": "PH",
        "short": "RP",
        "region": "Asia",
        "South-eastern Asia": "South-eastern Asia"
    },
    "PCN": {
        "name": "Pitcairn",
        "iso2": "PN",
        "short": "PC",
        "region": "Oceania",
        "Polynesia": "Polynesia"
    },
    "POL": {
        "name": "Poland",
        "iso2": "PL",
        "short": "PL",
        "region": "Europe",
        "Eastern Europe": "Eastern Europe"
    },
    "PRT": {
        "name": "Portugal",
        "iso2": "PT",
        "short": "PO",
        "region": "Europe",
        "Southern Europe": "Southern Europe"
    },
    "PRI": {
        "name": "Puerto Rico",
        "iso2": "PR",
        "short": "RQ",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "QAT": {
        "name": "Qatar",
        "iso2": "QA",
        "short": "QA",
        "region": "Asia",
        "Western Asia": "Western Asia"
    },
    "KOR": {
        "name": "Republic of Korea",
        "iso2": "KR",
        "short": "KS",
        "region": "Asia",
        "Eastern Asia": "Eastern Asia"
    },
    "MDA": {
        "name": "Republic of Moldova",
        "iso2": "MD",
        "short": "MD",
        "region": "Europe",
        "Eastern Europe": "Eastern Europe"
    },
    "ROU": {
        "name": "Romania",
        "iso2": "RO",
        "short": "RO",
        "region": "Europe",
        "Eastern Europe": "Eastern Europe"
    },
    "RUS": {
        "name": "Russian Federation",
        "iso2": "RU",
        "short": "RS",
        "region": "Europe",
        "Eastern Europe": "Eastern Europe"
    },
    "RWA": {
        "name": "Rwanda",
        "iso2": "RW",
        "short": "RW",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "REU": {
        "name": "R union",
        "iso2": "RE",
        "short": "RE",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "BLM": {
        "name": "Saint Barth lemy",
        "iso2": "BL",
        "short": "TB",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "SHN": {
        "name": "Saint Helena",
        "iso2": "SH",
        "short": "SH",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "KNA": {
        "name": "Saint Kitts and Nevis",
        "iso2": "KN",
        "short": "SC",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "LCA": {
        "name": "Saint Lucia",
        "iso2": "LC",
        "short": "ST",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "MAF": {
        "name": "Saint Martin (French Part)",
        "iso2": "MF",
        "short": "RN",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "SPM": {
        "name": "Saint Pierre and Miquelon",
        "iso2": "PM",
        "short": "SB",
        "region": "Americas",
        "Northern America": "Northern America"
    },
    "VCT": {
        "name": "Saint Vincent and the Grenadines",
        "iso2": "VC",
        "short": "VC",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "WSM": {
        "name": "Samoa",
        "iso2": "WS",
        "short": "WS",
        "region": "Oceania",
        "Polynesia": "Polynesia"
    },
    "SMR": {
        "name": "San Marino",
        "iso2": "SM",
        "short": "SM",
        "region": "Europe",
        "Southern Europe": "Southern Europe"
    },
    "STP": {
        "name": "Sao Tome and Principe",
        "iso2": "ST",
        "short": "TP",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "SAU": {
        "name": "Saudi Arabia",
        "iso2": "SA",
        "short": "SA",
        "region": "Asia",
        "Western Asia": "Western Asia"
    },
    "SEN": {
        "name": "Senegal",
        "iso2": "SN",
        "short": "SG",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "SYC": {
        "name": "Seychelles",
        "iso2": "SC",
        "short": "SE",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "SLE": {
        "name": "Sierra Leone",
        "iso2": "SL",
        "short": "SL",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "SGP": {
        "name": "Singapore",
        "iso2": "SG",
        "short": "SN",
        "region": "Asia",
        "South-eastern Asia": "South-eastern Asia"
    },
    "SXM": {
        "name": "Sint Maarten (Dutch part)",
        "iso2": "SX",
        "short": "NN",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "SVK": {
        "name": "Slovakia",
        "iso2": "SK",
        "short": "LO",
        "region": "Europe",
        "Eastern Europe": "Eastern Europe"
    },
    "SVN": {
        "name": "Slovenia",
        "iso2": "SI",
        "short": "SI",
        "region": "Europe",
        "Southern Europe": "Southern Europe"
    },
    "SLB": {
        "name": "Solomon Islands",
        "iso2": "SB",
        "short": "BP",
        "region": "Oceania",
        "Melanesia": "Melanesia"
    },
    "SOM": {
        "name": "Somalia",
        "iso2": "SO",
        "short": "SO",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "ZAF": {
        "name": "South Africa",
        "iso2": "ZA",
        "short": "SF",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "SGS": {
        "name": "South Georgia and the South Sandwich Islands",
        "iso2": "GS",
        "short": "SX",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "SSD": {
        "name": "South Sudan",
        "iso2": "SS",
        "short": "OD",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "ESP": {
        "name": "Spain",
        "iso2": "ES",
        "short": "SP",
        "region": "Europe",
        "Southern Europe": "Southern Europe"
    },
    "LKA": {
        "name": "Sri Lanka",
        "iso2": "LK",
        "short": "CE",
        "region": "Asia",
        "Southern Asia": "Southern Asia"
    },
    "SDN": {
        "name": "Sudan",
        "iso2": "SD",
        "short": "SU",
        "region": "Africa",
        "Northern Africa": "Northern Africa"
    },
    "SUR": {
        "name": "Suriname",
        "iso2": "SR",
        "short": "NS",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "SWZ": {
        "name": "Swaziland",
        "iso2": "SZ",
        "short": "WZ",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "SWE": {
        "name": "Sweden",
        "iso2": "SE",
        "short": "SW",
        "region": "Europe",
        "Northern Europe": "Northern Europe"
    },
    "CHE": {
        "name": "Switzerland",
        "iso2": "CH",
        "short": "SZ",
        "region": "Europe",
        "Western Europe": "Western Europe"
    },
    "SYR": {
        "name": "Syrian Arab Republic",
        "iso2": "SY",
        "short": "SY",
        "region": "Asia",
        "Western Asia": "Western Asia"
    },
    "TJK": {
        "name": "Tajikistan",
        "iso2": "TJ",
        "short": "TI",
        "region": "Asia",
        "Central Asia": "Central Asia"
    },
    "THA": {
        "name": "Thailand",
        "iso2": "TH",
        "short": "TH",
        "region": "Asia",
        "South-eastern Asia": "South-eastern Asia"
    },
    "MKD": {
        "name": "The former Yugoslav Republic of Macedonia",
        "iso2": "MK",
        "short": "MK",
        "region": "Europe",
        "Southern Europe": "Southern Europe"
    },
    "TLS": {
        "name": "Timor-Leste",
        "iso2": "TL",
        "short": "TT",
        "region": "Asia",
        "South-eastern Asia": "South-eastern Asia"
    },
    "TGO": {
        "name": "Togo",
        "iso2": "TG",
        "short": "TO",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "TKL": {
        "name": "Tokelau",
        "iso2": "TK",
        "short": "TL",
        "region": "Oceania",
        "Polynesia": "Polynesia"
    },
    "TON": {
        "name": "Tonga",
        "iso2": "TO",
        "short": "TN",
        "region": "Oceania",
        "Polynesia": "Polynesia"
    },
    "TTO": {
        "name": "Trinidad and Tobago",
        "iso2": "TT",
        "short": "TD",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "TUN": {
        "name": "Tunisia",
        "iso2": "TN",
        "short": "TS",
        "region": "Africa",
        "Northern Africa": "Northern Africa"
    },
    "TUR": {
        "name": "Turkey",
        "iso2": "TR",
        "short": "TU",
        "region": "Asia",
        "Western Asia": "Western Asia"
    },
    "TKM": {
        "name": "Turkmenistan",
        "iso2": "TM",
        "short": "TX",
        "region": "Asia",
        "Central Asia": "Central Asia"
    },
    "TCA": {
        "name": "Turks and Caicos Islands",
        "iso2": "TC",
        "short": "TK",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "TUV": {
        "name": "Tuvalu",
        "iso2": "TV",
        "short": "TV",
        "region": "Oceania",
        "Polynesia": "Polynesia"
    },
    "UGA": {
        "name": "Uganda",
        "iso2": "UG",
        "short": "UG",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "UKR": {
        "name": "Ukraine",
        "iso2": "UA",
        "short": "UP",
        "region": "Europe",
        "Eastern Europe": "Eastern Europe"
    },
    "ARE": {
        "name": "United Arab Emirates",
        "iso2": "AE",
        "short": "AE",
        "region": "Asia",
        "Western Asia": "Western Asia"
    },
    "GBR": {
        "name": "United Kingdom of Great Britain and Northern Ireland",
        "iso2": "GB",
        "short": "UK",
        "region": "Europe",
        "Northern Europe": "Northern Europe"
    },
    "TZA": {
        "name": "United Republic of Tanzania",
        "iso2": "TZ",
        "short": "TZ",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "VIR": {
        "name": "United States Virgin Islands",
        "iso2": "VI",
        "short": "VQ",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "USA": {
        "name": "United States of America",
        "iso2": "US",
        "short": "US",
        "region": "Americas",
        "Northern America": "Northern America"
    },
    "URY": {
        "name": "Uruguay",
        "iso2": "UY",
        "short": "UY",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "UZB": {
        "name": "Uzbekistan",
        "iso2": "UZ",
        "short": "UZ",
        "region": "Asia",
        "Central Asia": "Central Asia"
    },
    "VUT": {
        "name": "Vanuatu",
        "iso2": "VU",
        "short": "NH",
        "region": "Oceania",
        "Melanesia": "Melanesia"
    },
    "VEN": {
        "name": "Venezuela (Bolivarian Republic of)",
        "iso2": "VE",
        "short": "VE",
        "region": "Americas",
        "Latin America and the Caribbean": "Latin America and the Caribbean"
    },
    "VNM": {
        "name": "Viet Nam",
        "iso2": "VN",
        "short": "VM",
        "region": "Asia",
        "South-eastern Asia": "South-eastern Asia"
    },
    "WLF": {
        "name": "Wallis and Futuna Islands",
        "iso2": "WF",
        "short": "WF",
        "region": "Oceania",
        "Polynesia": "Polynesia"
    },
    "ESH": {
        "name": "Western Sahara",
        "iso2": "EH",
        "short": "WI",
        "region": "Africa",
        "Northern Africa": "Northern Africa"
    },
    "YEM": {
        "name": "Yemen",
        "iso2": "YE",
        "short": "YM",
        "region": "Asia",
        "Western Asia": "Western Asia"
    },
    "ZMB": {
        "name": "Zambia",
        "iso2": "ZM",
        "short": "ZA",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    },
    "ZWE": {
        "name": "Zimbabwe",
        "iso2": "ZW",
        "short": "ZI",
        "region": "Africa",
        "Sub-Saharan Africa": "Sub-Saharan Africa"
    }
}
