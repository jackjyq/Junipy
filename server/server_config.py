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
        "subregion": "Southern Asia"
    },
    "ALB": {
        "name": "Albania",
        "iso2": "AL",
        "short": "AL",
        "region": "Europe",
        "subregion": "Southern Europe"
    },
    "DZA": {
        "name": "Algeria",
        "iso2": "DZ",
        "short": "AG",
        "region": "Africa",
        "subregion": "Northern Africa"
    },
    "ASM": {
        "name": "American Samoa",
        "iso2": "AS",
        "short": "AQ",
        "region": "Oceania",
        "subregion": "Polynesia"
    },
    "AND": {
        "name": "Andorra",
        "iso2": "AD",
        "short": "AN",
        "region": "Europe",
        "subregion": "Southern Europe"
    },
    "AGO": {
        "name": "Angola",
        "iso2": "AO",
        "short": "AO",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "AIA": {
        "name": "Anguilla",
        "iso2": "AI",
        "short": "AV",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "ATA": {
        "name": "Antarctica",
        "iso2": "AQ",
        "short": "AY",
        "region": "Antarctica",
        "subregion": "Antarctica"
    },
    "ATG": {
        "name": "Antigua and Barbuda",
        "iso2": "AG",
        "short": "AC",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "ARG": {
        "name": "Argentina",
        "iso2": "AR",
        "short": "AR",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "ARM": {
        "name": "Armenia",
        "iso2": "AM",
        "short": "AM",
        "region": "Asia",
        "subregion": "Western Asia"
    },
    "ABW": {
        "name": "Aruba",
        "iso2": "AW",
        "short": "AA",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "AUS": {
        "name": "Australia",
        "iso2": "AU",
        "short": "AS",
        "region": "Oceania",
        "subregion": "Australia and New Zealand"
    },
    "AUT": {
        "name": "Austria",
        "iso2": "AT",
        "short": "AU",
        "region": "Europe",
        "subregion": "Western Europe"
    },
    "AZE": {
        "name": "Azerbaijan",
        "iso2": "AZ",
        "short": "AJ",
        "region": "Asia",
        "subregion": "Western Asia"
    },
    "BHS": {
        "name": "Bahamas",
        "iso2": "BS",
        "short": "BF",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "BHR": {
        "name": "Bahrain",
        "iso2": "BH",
        "short": "BA",
        "region": "Asia",
        "subregion": "Western Asia"
    },
    "BGD": {
        "name": "Bangladesh",
        "iso2": "BD",
        "short": "BG",
        "region": "Asia",
        "subregion": "Southern Asia"
    },
    "BRB": {
        "name": "Barbados",
        "iso2": "BB",
        "short": "BB",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "BLR": {
        "name": "Belarus",
        "iso2": "BY",
        "short": "BO",
        "region": "Europe",
        "subregion": "Eastern Europe"
    },
    "BEL": {
        "name": "Belgium",
        "iso2": "BE",
        "short": "BE",
        "region": "Europe",
        "subregion": "Western Europe"
    },
    "BLZ": {
        "name": "Belize",
        "iso2": "BZ",
        "short": "BH",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "BEN": {
        "name": "Benin",
        "iso2": "BJ",
        "short": "BN",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "BMU": {
        "name": "Bermuda",
        "iso2": "BM",
        "short": "BD",
        "region": "Americas",
        "subregion": "Northern America"
    },
    "BTN": {
        "name": "Bhutan",
        "iso2": "BT",
        "short": "BT",
        "region": "Asia",
        "subregion": "Southern Asia"
    },
    "BOL": {
        "name": "Bolivia (Plurinational State of)",
        "iso2": "BO",
        "short": "BL",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "BES": {
        "name": "Bonaire, Sint Eustatius and Saba",
        "iso2": "BQ",
        "short": "NL",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "BIH": {
        "name": "Bosnia and Herzegovina",
        "iso2": "BA",
        "short": "BK",
        "region": "Europe",
        "subregion": "Southern Europe"
    },
    "BWA": {
        "name": "Botswana",
        "iso2": "BW",
        "short": "BC",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "BVT": {
        "name": "Bouvet Island",
        "iso2": "BV",
        "short": "BV",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "BRA": {
        "name": "Brazil",
        "iso2": "BR",
        "short": "BR",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "IOT": {
        "name": "British Indian Ocean Territory",
        "iso2": "IO",
        "short": "IO",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "VGB": {
        "name": "British Virgin Islands",
        "iso2": "VG",
        "short": "VI",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "BRN": {
        "name": "Brunei Darussalam",
        "iso2": "BN",
        "short": "BX",
        "region": "Asia",
        "subregion": "South-eastern Asia"
    },
    "BGR": {
        "name": "Bulgaria",
        "iso2": "BG",
        "short": "BU",
        "region": "Europe",
        "subregion": "Eastern Europe"
    },
    "BFA": {
        "name": "Burkina Faso",
        "iso2": "BF",
        "short": "UV",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "BDI": {
        "name": "Burundi",
        "iso2": "BI",
        "short": "BY",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "CPV": {
        "name": "Cabo Verde",
        "iso2": "CV",
        "short": "CV",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "KHM": {
        "name": "Cambodia",
        "iso2": "KH",
        "short": "CB",
        "region": "Asia",
        "subregion": "South-eastern Asia"
    },
    "CMR": {
        "name": "Cameroon",
        "iso2": "CM",
        "short": "CM",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "CAN": {
        "name": "Canada",
        "iso2": "CA",
        "short": "CA",
        "region": "Americas",
        "subregion": "Northern America"
    },
    "CYM": {
        "name": "Cayman Islands",
        "iso2": "KY",
        "short": "CJ",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "CAF": {
        "name": "Central African Republic",
        "iso2": "CF",
        "short": "CT",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "TCD": {
        "name": "Chad",
        "iso2": "TD",
        "short": "CD",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "CHL": {
        "name": "Chile",
        "iso2": "CL",
        "short": "CI",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "CHN": {
        "name": "China",
        "iso2": "CN",
        "short": "CH",
        "region": "Asia",
        "subregion": "Eastern Asia"
    },
    "HKG": {
        "name": "China, Hong Kong Special Administrative Region",
        "iso2": "HK",
        "short": "HK",
        "region": "Asia",
        "subregion": "Eastern Asia"
    },
    "MAC": {
        "name": "China, Macao Special Administrative Region",
        "iso2": "MO",
        "short": "MC",
        "region": "Asia",
        "subregion": "Eastern Asia"
    },
    "CXR": {
        "name": "Christmas Island",
        "iso2": "CX",
        "short": "KT",
        "region": "Oceania",
        "subregion": "Australia and New Zealand"
    },
    "CCK": {
        "name": "Cocos (Keeling) Islands",
        "iso2": "CC",
        "short": "CK",
        "region": "Oceania",
        "subregion": "Australia and New Zealand"
    },
    "COL": {
        "name": "Colombia",
        "iso2": "CO",
        "short": "CO",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "COM": {
        "name": "Comoros",
        "iso2": "KM",
        "short": "CN",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "COG": {
        "name": "Congo",
        "iso2": "CG",
        "short": "CF",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "COK": {
        "name": "Cook Islands",
        "iso2": "CK",
        "short": "CW",
        "region": "Oceania",
        "subregion": "Polynesia"
    },
    "CRI": {
        "name": "Costa Rica",
        "iso2": "CR",
        "short": "CS",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "HRV": {
        "name": "Croatia",
        "iso2": "HR",
        "short": "HR",
        "region": "Europe",
        "subregion": "Southern Europe"
    },
    "CUB": {
        "name": "Cuba",
        "iso2": "CU",
        "short": "CU",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "CUW": {
        "name": "Cura ao",
        "iso2": "CW",
        "short": "UC",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "CYP": {
        "name": "Cyprus",
        "iso2": "CY",
        "short": "CY",
        "region": "Asia",
        "subregion": "Western Asia"
    },
    "CZE": {
        "name": "Czechia",
        "iso2": "CZ",
        "short": "EZ",
        "region": "Europe",
        "subregion": "Eastern Europe"
    },
    "CIV": {
        "name": "C te d'Ivoire",
        "iso2": "CI",
        "short": "IV",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "PRK": {
        "name": "Democratic People's Republic of Korea",
        "iso2": "KP",
        "short": "KN",
        "region": "Asia",
        "subregion": "Eastern Asia"
    },
    "COD": {
        "name": "Democratic Republic of the Congo",
        "iso2": "CD",
        "short": "CG",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "DNK": {
        "name": "Denmark",
        "iso2": "DK",
        "short": "DA",
        "region": "Europe",
        "subregion": "Northern Europe"
    },
    "DJI": {
        "name": "Djibouti",
        "iso2": "DJ",
        "short": "DJ",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "DMA": {
        "name": "Dominica",
        "iso2": "DM",
        "short": "DO",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "DOM": {
        "name": "Dominican Republic",
        "iso2": "DO",
        "short": "DR",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "ECU": {
        "name": "Ecuador",
        "iso2": "EC",
        "short": "EC",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "EGY": {
        "name": "Egypt",
        "iso2": "EG",
        "short": "EG",
        "region": "Africa",
        "subregion": "Northern Africa"
    },
    "SLV": {
        "name": "El Salvador",
        "iso2": "SV",
        "short": "ES",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "GNQ": {
        "name": "Equatorial Guinea",
        "iso2": "GQ",
        "short": "EK",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "ERI": {
        "name": "Eritrea",
        "iso2": "ER",
        "short": "ER",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "EST": {
        "name": "Estonia",
        "iso2": "EE",
        "short": "EN",
        "region": "Europe",
        "subregion": "Northern Europe"
    },
    "ETH": {
        "name": "Ethiopia",
        "iso2": "ET",
        "short": "ET",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "FLK": {
        "name": "Falkland Islands (Malvinas)",
        "iso2": "FK",
        "short": "FK",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "FRO": {
        "name": "Faroe Islands",
        "iso2": "FO",
        "short": "FO",
        "region": "Europe",
        "subregion": "Northern Europe"
    },
    "FJI": {
        "name": "Fiji",
        "iso2": "FJ",
        "short": "FJ",
        "region": "Oceania",
        "subregion": "Melanesia"
    },
    "FIN": {
        "name": "Finland",
        "iso2": "FI",
        "short": "FI",
        "region": "Europe",
        "subregion": "Northern Europe"
    },
    "FRA": {
        "name": "France",
        "iso2": "FR",
        "short": "FR",
        "region": "Europe",
        "subregion": "Western Europe"
    },
    "GUF": {
        "name": "French Guiana",
        "iso2": "GF",
        "short": "FG",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "PYF": {
        "name": "French Polynesia",
        "iso2": "PF",
        "short": "FP",
        "region": "Oceania",
        "subregion": "Polynesia"
    },
    "ATF": {
        "name": "French Southern Territories",
        "iso2": "TF",
        "short": "FS",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "GAB": {
        "name": "Gabon",
        "iso2": "GA",
        "short": "GB",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "GMB": {
        "name": "Gambia",
        "iso2": "GM",
        "short": "GA",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "GEO": {
        "name": "Georgia",
        "iso2": "GE",
        "short": "GG",
        "region": "Asia",
        "subregion": "Western Asia"
    },
    "DEU": {
        "name": "Germany",
        "iso2": "DE",
        "short": "GM",
        "region": "Europe",
        "subregion": "Western Europe"
    },
    "GHA": {
        "name": "Ghana",
        "iso2": "GH",
        "short": "GH",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "GIB": {
        "name": "Gibraltar",
        "iso2": "GI",
        "short": "GI",
        "region": "Europe",
        "subregion": "Southern Europe"
    },
    "GRC": {
        "name": "Greece",
        "iso2": "GR",
        "short": "GR",
        "region": "Europe",
        "subregion": "Southern Europe"
    },
    "GRL": {
        "name": "Greenland",
        "iso2": "GL",
        "short": "GL",
        "region": "Americas",
        "subregion": "Northern America"
    },
    "GRD": {
        "name": "Grenada",
        "iso2": "GD",
        "short": "GJ",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "GLP": {
        "name": "Guadeloupe",
        "iso2": "GP",
        "short": "GP",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "GUM": {
        "name": "Guam",
        "iso2": "GU",
        "short": "GQ",
        "region": "Oceania",
        "subregion": "Micronesia"
    },
    "GTM": {
        "name": "Guatemala",
        "iso2": "GT",
        "short": "GT",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "GGY": {
        "name": "Guernsey",
        "iso2": "GG",
        "short": "GK",
        "region": "Europe",
        "subregion": "Northern Europe"
    },
    "GIN": {
        "name": "Guinea",
        "iso2": "GN",
        "short": "GV",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "GNB": {
        "name": "Guinea-Bissau",
        "iso2": "GW",
        "short": "PU",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "GUY": {
        "name": "Guyana",
        "iso2": "GY",
        "short": "GY",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "HTI": {
        "name": "Haiti",
        "iso2": "HT",
        "short": "HA",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "HMD": {
        "name": "Heard Island and McDonald Islands",
        "iso2": "HM",
        "short": "HM",
        "region": "Oceania",
        "subregion": "Australia and New Zealand"
    },
    "VAT": {
        "name": "Holy See",
        "iso2": "VA",
        "short": "VT",
        "region": "Europe",
        "subregion": "Southern Europe"
    },
    "HND": {
        "name": "Honduras",
        "iso2": "HN",
        "short": "HO",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "HUN": {
        "name": "Hungary",
        "iso2": "HU",
        "short": "HU",
        "region": "Europe",
        "subregion": "Eastern Europe"
    },
    "ISL": {
        "name": "Iceland",
        "iso2": "IS",
        "short": "IC",
        "region": "Europe",
        "subregion": "Northern Europe"
    },
    "IND": {
        "name": "India",
        "iso2": "IN",
        "short": "IN",
        "region": "Asia",
        "subregion": "Southern Asia"
    },
    "IDN": {
        "name": "Indonesia",
        "iso2": "ID",
        "short": "ID",
        "region": "Asia",
        "subregion": "South-eastern Asia"
    },
    "IRN": {
        "name": "Iran (Islamic Republic of)",
        "iso2": "IR",
        "short": "IR",
        "region": "Asia",
        "subregion": "Southern Asia"
    },
    "IRQ": {
        "name": "Iraq",
        "iso2": "IQ",
        "short": "IZ",
        "region": "Asia",
        "subregion": "Western Asia"
    },
    "IRL": {
        "name": "Ireland",
        "iso2": "IE",
        "short": "EI",
        "region": "Europe",
        "subregion": "Northern Europe"
    },
    "IMN": {
        "name": "Isle of Man",
        "iso2": "IM",
        "short": "IM",
        "region": "Europe",
        "subregion": "Northern Europe"
    },
    "ISR": {
        "name": "Israel",
        "iso2": "IL",
        "short": "IS",
        "region": "Asia",
        "subregion": "Western Asia"
    },
    "ITA": {
        "name": "Italy",
        "iso2": "IT",
        "short": "IT",
        "region": "Europe",
        "subregion": "Southern Europe"
    },
    "JAM": {
        "name": "Jamaica",
        "iso2": "JM",
        "short": "JM",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "JPN": {
        "name": "Japan",
        "iso2": "JP",
        "short": "JA",
        "region": "Asia",
        "subregion": "Eastern Asia"
    },
    "JEY": {
        "name": "Jersey",
        "iso2": "JE",
        "short": "JE",
        "region": "Europe",
        "subregion": "Northern Europe"
    },
    "JOR": {
        "name": "Jordan",
        "iso2": "JO",
        "short": "JO",
        "region": "Asia",
        "subregion": "Western Asia"
    },
    "KAZ": {
        "name": "Kazakhstan",
        "iso2": "KZ",
        "short": "KZ",
        "region": "Asia",
        "subregion": "Central Asia"
    },
    "KEN": {
        "name": "Kenya",
        "iso2": "KE",
        "short": "KE",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "KIR": {
        "name": "Kiribati",
        "iso2": "KI",
        "short": "KR",
        "region": "Oceania",
        "subregion": "Micronesia"
    },
    "KWT": {
        "name": "Kuwait",
        "iso2": "KW",
        "short": "KU",
        "region": "Asia",
        "subregion": "Western Asia"
    },
    "KGZ": {
        "name": "Kyrgyzstan",
        "iso2": "KG",
        "short": "KG",
        "region": "Asia",
        "subregion": "Central Asia"
    },
    "LAO": {
        "name": "Lao People's Democratic Republic",
        "iso2": "LA",
        "short": "LA",
        "region": "Asia",
        "subregion": "South-eastern Asia"
    },
    "LVA": {
        "name": "Latvia",
        "iso2": "LV",
        "short": "LG",
        "region": "Europe",
        "subregion": "Northern Europe"
    },
    "LBN": {
        "name": "Lebanon",
        "iso2": "LB",
        "short": "LE",
        "region": "Asia",
        "subregion": "Western Asia"
    },
    "LSO": {
        "name": "Lesotho",
        "iso2": "LS",
        "short": "LT",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "LBR": {
        "name": "Liberia",
        "iso2": "LR",
        "short": "LI",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "LBY": {
        "name": "Libya",
        "iso2": "LY",
        "short": "LY",
        "region": "Africa",
        "subregion": "Northern Africa"
    },
    "LIE": {
        "name": "Liechtenstein",
        "iso2": "LI",
        "short": "LS",
        "region": "Europe",
        "subregion": "Western Europe"
    },
    "LTU": {
        "name": "Lithuania",
        "iso2": "LT",
        "short": "LH",
        "region": "Europe",
        "subregion": "Northern Europe"
    },
    "LUX": {
        "name": "Luxembourg",
        "iso2": "LU",
        "short": "LU",
        "region": "Europe",
        "subregion": "Western Europe"
    },
    "MDG": {
        "name": "Madagascar",
        "iso2": "MG",
        "short": "MA",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "MWI": {
        "name": "Malawi",
        "iso2": "MW",
        "short": "MI",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "MYS": {
        "name": "Malaysia",
        "iso2": "MY",
        "short": "MY",
        "region": "Asia",
        "subregion": "South-eastern Asia"
    },
    "MDV": {
        "name": "Maldives",
        "iso2": "MV",
        "short": "MV",
        "region": "Asia",
        "subregion": "Southern Asia"
    },
    "MLI": {
        "name": "Mali",
        "iso2": "ML",
        "short": "ML",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "MLT": {
        "name": "Malta",
        "iso2": "MT",
        "short": "MT",
        "region": "Europe",
        "subregion": "Southern Europe"
    },
    "MHL": {
        "name": "Marshall Islands",
        "iso2": "MH",
        "short": "RM",
        "region": "Oceania",
        "subregion": "Micronesia"
    },
    "MTQ": {
        "name": "Martinique",
        "iso2": "MQ",
        "short": "MB",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "MRT": {
        "name": "Mauritania",
        "iso2": "MR",
        "short": "MR",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "MUS": {
        "name": "Mauritius",
        "iso2": "MU",
        "short": "MP",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "MYT": {
        "name": "Mayotte",
        "iso2": "YT",
        "short": "MF",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "MEX": {
        "name": "Mexico",
        "iso2": "MX",
        "short": "MX",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "FSM": {
        "name": "Micronesia (Federated States of)",
        "iso2": "FM",
        "short": "FM",
        "region": "Oceania",
        "subregion": "Micronesia"
    },
    "MCO": {
        "name": "Monaco",
        "iso2": "MC",
        "short": "MN",
        "region": "Europe",
        "subregion": "Western Europe"
    },
    "MNG": {
        "name": "Mongolia",
        "iso2": "MN",
        "short": "MG",
        "region": "Asia",
        "subregion": "Eastern Asia"
    },
    "MNE": {
        "name": "Montenegro",
        "iso2": "ME",
        "short": "MJ",
        "region": "Europe",
        "subregion": "Southern Europe"
    },
    "MSR": {
        "name": "Montserrat",
        "iso2": "MS",
        "short": "MH",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "MAR": {
        "name": "Morocco",
        "iso2": "MA",
        "short": "MO",
        "region": "Africa",
        "subregion": "Northern Africa"
    },
    "MOZ": {
        "name": "Mozambique",
        "iso2": "MZ",
        "short": "MZ",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "MMR": {
        "name": "Myanmar",
        "iso2": "MM",
        "short": "BM",
        "region": "Asia",
        "subregion": "South-eastern Asia"
    },
    "NAM": {
        "name": "Namibia",
        "iso2": "NA",
        "short": "WA",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "NRU": {
        "name": "Nauru",
        "iso2": "NR",
        "short": "NR",
        "region": "Oceania",
        "subregion": "Micronesia"
    },
    "NPL": {
        "name": "Nepal",
        "iso2": "NP",
        "short": "NP",
        "region": "Asia",
        "subregion": "Southern Asia"
    },
    "NLD": {
        "name": "Netherlands",
        "iso2": "NL",
        "short": "NL",
        "region": "Europe",
        "subregion": "Western Europe"
    },
    "NCL": {
        "name": "New Caledonia",
        "iso2": "NC",
        "short": "NC",
        "region": "Oceania",
        "subregion": "Melanesia"
    },
    "NZL": {
        "name": "New Zealand",
        "iso2": "NZ",
        "short": "NZ",
        "region": "Oceania",
        "subregion": "Australia and New Zealand"
    },
    "NIC": {
        "name": "Nicaragua",
        "iso2": "NI",
        "short": "NU",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "NER": {
        "name": "Niger",
        "iso2": "NE",
        "short": "NG",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "NGA": {
        "name": "Nigeria",
        "iso2": "NG",
        "short": "NI",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "NIU": {
        "name": "Niue",
        "iso2": "NU",
        "short": "NE",
        "region": "Oceania",
        "subregion": "Polynesia"
    },
    "NFK": {
        "name": "Norfolk Island",
        "iso2": "NF",
        "short": "NF",
        "region": "Oceania",
        "subregion": "Australia and New Zealand"
    },
    "MNP": {
        "name": "Northern Mariana Islands",
        "iso2": "MP",
        "short": "CQ",
        "region": "Oceania",
        "subregion": "Micronesia"
    },
    "NOR": {
        "name": "Norway",
        "iso2": "NO",
        "short": "NO",
        "region": "Europe",
        "subregion": "Northern Europe"
    },
    "OMN": {
        "name": "Oman",
        "iso2": "OM",
        "short": "MU",
        "region": "Asia",
        "subregion": "Western Asia"
    },
    "PAK": {
        "name": "Pakistan",
        "iso2": "PK",
        "short": "PK",
        "region": "Asia",
        "subregion": "Southern Asia"
    },
    "PLW": {
        "name": "Palau",
        "iso2": "PW",
        "short": "PS",
        "region": "Oceania",
        "subregion": "Micronesia"
    },
    "PAN": {
        "name": "Panama",
        "iso2": "PA",
        "short": "PM",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "PNG": {
        "name": "Papua New Guinea",
        "iso2": "PG",
        "short": "PP",
        "region": "Oceania",
        "subregion": "Melanesia"
    },
    "PRY": {
        "name": "Paraguay",
        "iso2": "PY",
        "short": "PA",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "PER": {
        "name": "Peru",
        "iso2": "PE",
        "short": "PE",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "PHL": {
        "name": "Philippines",
        "iso2": "PH",
        "short": "RP",
        "region": "Asia",
        "subregion": "South-eastern Asia"
    },
    "PCN": {
        "name": "Pitcairn",
        "iso2": "PN",
        "short": "PC",
        "region": "Oceania",
        "subregion": "Polynesia"
    },
    "POL": {
        "name": "Poland",
        "iso2": "PL",
        "short": "PL",
        "region": "Europe",
        "subregion": "Eastern Europe"
    },
    "PRT": {
        "name": "Portugal",
        "iso2": "PT",
        "short": "PO",
        "region": "Europe",
        "subregion": "Southern Europe"
    },
    "PRI": {
        "name": "Puerto Rico",
        "iso2": "PR",
        "short": "RQ",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "QAT": {
        "name": "Qatar",
        "iso2": "QA",
        "short": "QA",
        "region": "Asia",
        "subregion": "Western Asia"
    },
    "KOR": {
        "name": "Republic of Korea",
        "iso2": "KR",
        "short": "KS",
        "region": "Asia",
        "subregion": "Eastern Asia"
    },
    "MDA": {
        "name": "Republic of Moldova",
        "iso2": "MD",
        "short": "MD",
        "region": "Europe",
        "subregion": "Eastern Europe"
    },
    "ROU": {
        "name": "Romania",
        "iso2": "RO",
        "short": "RO",
        "region": "Europe",
        "subregion": "Eastern Europe"
    },
    "RUS": {
        "name": "Russian Federation",
        "iso2": "RU",
        "short": "RS",
        "region": "Europe",
        "subregion": "Eastern Europe"
    },
    "RWA": {
        "name": "Rwanda",
        "iso2": "RW",
        "short": "RW",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "REU": {
        "name": "R union",
        "iso2": "RE",
        "short": "RE",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "BLM": {
        "name": "Saint Barth lemy",
        "iso2": "BL",
        "short": "TB",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "SHN": {
        "name": "Saint Helena",
        "iso2": "SH",
        "short": "SH",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "KNA": {
        "name": "Saint Kitts and Nevis",
        "iso2": "KN",
        "short": "SC",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "LCA": {
        "name": "Saint Lucia",
        "iso2": "LC",
        "short": "ST",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "MAF": {
        "name": "Saint Martin (French Part)",
        "iso2": "MF",
        "short": "RN",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "SPM": {
        "name": "Saint Pierre and Miquelon",
        "iso2": "PM",
        "short": "SB",
        "region": "Americas",
        "subregion": "Northern America"
    },
    "VCT": {
        "name": "Saint Vincent and the Grenadines",
        "iso2": "VC",
        "short": "VC",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "WSM": {
        "name": "Samoa",
        "iso2": "WS",
        "short": "WS",
        "region": "Oceania",
        "subregion": "Polynesia"
    },
    "SMR": {
        "name": "San Marino",
        "iso2": "SM",
        "short": "SM",
        "region": "Europe",
        "subregion": "Southern Europe"
    },
    "STP": {
        "name": "Sao Tome and Principe",
        "iso2": "ST",
        "short": "TP",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "SAU": {
        "name": "Saudi Arabia",
        "iso2": "SA",
        "short": "SA",
        "region": "Asia",
        "subregion": "Western Asia"
    },
    "SEN": {
        "name": "Senegal",
        "iso2": "SN",
        "short": "SG",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "SYC": {
        "name": "Seychelles",
        "iso2": "SC",
        "short": "SE",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "SLE": {
        "name": "Sierra Leone",
        "iso2": "SL",
        "short": "SL",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "SGP": {
        "name": "Singapore",
        "iso2": "SG",
        "short": "SN",
        "region": "Asia",
        "subregion": "South-eastern Asia"
    },
    "SXM": {
        "name": "Sint Maarten (Dutch part)",
        "iso2": "SX",
        "short": "NN",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "SVK": {
        "name": "Slovakia",
        "iso2": "SK",
        "short": "LO",
        "region": "Europe",
        "subregion": "Eastern Europe"
    },
    "SVN": {
        "name": "Slovenia",
        "iso2": "SI",
        "short": "SI",
        "region": "Europe",
        "subregion": "Southern Europe"
    },
    "SLB": {
        "name": "Solomon Islands",
        "iso2": "SB",
        "short": "BP",
        "region": "Oceania",
        "subregion": "Melanesia"
    },
    "SOM": {
        "name": "Somalia",
        "iso2": "SO",
        "short": "SO",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "ZAF": {
        "name": "South Africa",
        "iso2": "ZA",
        "short": "SF",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "SGS": {
        "name": "South Georgia and the South Sandwich Islands",
        "iso2": "GS",
        "short": "SX",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "SSD": {
        "name": "South Sudan",
        "iso2": "SS",
        "short": "OD",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "ESP": {
        "name": "Spain",
        "iso2": "ES",
        "short": "SP",
        "region": "Europe",
        "subregion": "Southern Europe"
    },
    "LKA": {
        "name": "Sri Lanka",
        "iso2": "LK",
        "short": "CE",
        "region": "Asia",
        "subregion": "Southern Asia"
    },
    "SDN": {
        "name": "Sudan",
        "iso2": "SD",
        "short": "SU",
        "region": "Africa",
        "subregion": "Northern Africa"
    },
    "SUR": {
        "name": "Suriname",
        "iso2": "SR",
        "short": "NS",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "SWZ": {
        "name": "Swaziland",
        "iso2": "SZ",
        "short": "WZ",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "SWE": {
        "name": "Sweden",
        "iso2": "SE",
        "short": "SW",
        "region": "Europe",
        "subregion": "Northern Europe"
    },
    "CHE": {
        "name": "Switzerland",
        "iso2": "CH",
        "short": "SZ",
        "region": "Europe",
        "subregion": "Western Europe"
    },
    "SYR": {
        "name": "Syrian Arab Republic",
        "iso2": "SY",
        "short": "SY",
        "region": "Asia",
        "subregion": "Western Asia"
    },
    "TJK": {
        "name": "Tajikistan",
        "iso2": "TJ",
        "short": "TI",
        "region": "Asia",
        "subregion": "Central Asia"
    },
    "THA": {
        "name": "Thailand",
        "iso2": "TH",
        "short": "TH",
        "region": "Asia",
        "subregion": "South-eastern Asia"
    },
    "MKD": {
        "name": "The former Yugoslav Republic of Macedonia",
        "iso2": "MK",
        "short": "MK",
        "region": "Europe",
        "subregion": "Southern Europe"
    },
    "TLS": {
        "name": "Timor-Leste",
        "iso2": "TL",
        "short": "TT",
        "region": "Asia",
        "subregion": "South-eastern Asia"
    },
    "TGO": {
        "name": "Togo",
        "iso2": "TG",
        "short": "TO",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "TKL": {
        "name": "Tokelau",
        "iso2": "TK",
        "short": "TL",
        "region": "Oceania",
        "subregion": "Polynesia"
    },
    "TON": {
        "name": "Tonga",
        "iso2": "TO",
        "short": "TN",
        "region": "Oceania",
        "subregion": "Polynesia"
    },
    "TTO": {
        "name": "Trinidad and Tobago",
        "iso2": "TT",
        "short": "TD",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "TUN": {
        "name": "Tunisia",
        "iso2": "TN",
        "short": "TS",
        "region": "Africa",
        "subregion": "Northern Africa"
    },
    "TUR": {
        "name": "Turkey",
        "iso2": "TR",
        "short": "TU",
        "region": "Asia",
        "subregion": "Western Asia"
    },
    "TKM": {
        "name": "Turkmenistan",
        "iso2": "TM",
        "short": "TX",
        "region": "Asia",
        "subregion": "Central Asia"
    },
    "TCA": {
        "name": "Turks and Caicos Islands",
        "iso2": "TC",
        "short": "TK",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "TUV": {
        "name": "Tuvalu",
        "iso2": "TV",
        "short": "TV",
        "region": "Oceania",
        "subregion": "Polynesia"
    },
    "UGA": {
        "name": "Uganda",
        "iso2": "UG",
        "short": "UG",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "UKR": {
        "name": "Ukraine",
        "iso2": "UA",
        "short": "UP",
        "region": "Europe",
        "subregion": "Eastern Europe"
    },
    "ARE": {
        "name": "United Arab Emirates",
        "iso2": "AE",
        "short": "AE",
        "region": "Asia",
        "subregion": "Western Asia"
    },
    "GBR": {
        "name": "United Kingdom of Great Britain and Northern Ireland",
        "iso2": "GB",
        "short": "UK",
        "region": "Europe",
        "subregion": "Northern Europe"
    },
    "TZA": {
        "name": "United Republic of Tanzania",
        "iso2": "TZ",
        "short": "TZ",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "VIR": {
        "name": "United States Virgin Islands",
        "iso2": "VI",
        "short": "VQ",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "USA": {
        "name": "United States of America",
        "iso2": "US",
        "short": "US",
        "region": "Americas",
        "subregion": "Northern America"
    },
    "URY": {
        "name": "Uruguay",
        "iso2": "UY",
        "short": "UY",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "UZB": {
        "name": "Uzbekistan",
        "iso2": "UZ",
        "short": "UZ",
        "region": "Asia",
        "subregion": "Central Asia"
    },
    "VUT": {
        "name": "Vanuatu",
        "iso2": "VU",
        "short": "NH",
        "region": "Oceania",
        "subregion": "Melanesia"
    },
    "VEN": {
        "name": "Venezuela (Bolivarian Republic of)",
        "iso2": "VE",
        "short": "VE",
        "region": "Americas",
        "subregion": "Latin America and the Caribbean"
    },
    "VNM": {
        "name": "Viet Nam",
        "iso2": "VN",
        "short": "VM",
        "region": "Asia",
        "subregion": "South-eastern Asia"
    },
    "WLF": {
        "name": "Wallis and Futuna Islands",
        "iso2": "WF",
        "short": "WF",
        "region": "Oceania",
        "subregion": "Polynesia"
    },
    "ESH": {
        "name": "Western Sahara",
        "iso2": "EH",
        "short": "WI",
        "region": "Africa",
        "subregion": "Northern Africa"
    },
    "YEM": {
        "name": "Yemen",
        "iso2": "YE",
        "short": "YM",
        "region": "Asia",
        "subregion": "Western Asia"
    },
    "ZMB": {
        "name": "Zambia",
        "iso2": "ZM",
        "short": "ZA",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    },
    "ZWE": {
        "name": "Zimbabwe",
        "iso2": "ZW",
        "short": "ZI",
        "region": "Africa",
        "subregion": "Sub-Saharan Africa"
    }
}