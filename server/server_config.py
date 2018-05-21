
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
    "KWT": {
        "name": "Kuwait",
        "iso2": "KW",
        "short": "KU"
    },
    "CRI": {
        "name": "Costa Rica",
        "iso2": "CR",
        "short": "CS"
    },
    "NOR": {
        "name": "Norway",
        "iso2": "NO",
        "short": "NO"
    },
    "AGO": {
        "name": "Angola",
        "iso2": "AO",
        "short": "AO"
    },
    "HRV": {
        "name": "Croatia",
        "iso2": "HR",
        "short": "HR"
    },
    "ZMB": {
        "name": "Zambia",
        "iso2": "ZM",
        "short": "ZA"
    },
    "GHA": {
        "name": "Ghana",
        "iso2": "GH",
        "short": "GH"
    },
    "PNG": {
        "name": "Papua New Guinea",
        "iso2": "PG",
        "short": "PP"
    },
    "MDV": {
        "name": "Maldives",
        "iso2": "MV",
        "short": "MV"
    },
    "MLI": {
        "name": "Mali",
        "iso2": "ML",
        "short": "ML"
    },
    "SWZ": {
        "name": "Swaziland",
        "iso2": "SZ",
        "short": "WZ"
    },
    "QAT": {
        "name": "Qatar",
        "iso2": "QA",
        "short": "QA"
    },
    "URY": {
        "name": "Uruguay",
        "iso2": "UY",
        "short": "UY"
    },
    "RWA": {
        "name": "Rwanda",
        "iso2": "RW",
        "short": "RW"
    },
    "SAU": {
        "name": "Saudi Arabia",
        "iso2": "SA",
        "short": "SA"
    },
    "EGY": {
        "name": "Egypt",
        "iso2": "EG",
        "short": "EG"
    },
    "MMR": {
        "name": "Myanmar",
        "iso2": "MM",
        "short": "BM"
    },
    "TCD": {
        "name": "Chad",
        "iso2": "TD",
        "short": "CD"
    },
    "DOM": {
        "name": "Dominican Republic",
        "iso2": "DO",
        "short": "DR"
    },
    "PHL": {
        "name": "Philippines",
        "iso2": "PH",
        "short": "RP"
    },
    "COL": {
        "name": "Colombia",
        "iso2": "CO",
        "short": "CO"
    },
    "LVA": {
        "name": "Latvia",
        "iso2": "LV",
        "short": "LG"
    },
    "MEX": {
        "name": "Mexico",
        "iso2": "MX",
        "short": "MX"
    },
    "COM": {
        "name": "Comoros",
        "iso2": "KM",
        "short": "CN"
    },
    "BTN": {
        "name": "Bhutan",
        "iso2": "BT",
        "short": "BT"
    },
    "BRB": {
        "name": "Barbados",
        "iso2": "BB",
        "short": "BB"
    },
    "SLV": {
        "name": "El Salvador",
        "iso2": "SV",
        "short": "ES"
    },
    "ETH": {
        "name": "Ethiopia",
        "iso2": "ET",
        "short": "ET"
    },
    "BEN": {
        "name": "Benin",
        "iso2": "BJ",
        "short": "BN"
    },
    "BOL": {
        "name": "Bolivia (Plurinational State of)",
        "iso2": "BO",
        "short": "BL"
    },
    "BFA": {
        "name": "Burkina Faso",
        "iso2": "BF",
        "short": "UV"
    },
    "BWA": {
        "name": "Botswana",
        "iso2": "BW",
        "short": "BC"
    },
    "BGD": {
        "name": "Bangladesh",
        "iso2": "BD",
        "short": "BG"
    },
    "BHS": {
        "name": "Bahamas",
        "iso2": "BS",
        "short": "BF"
    },
    "KHM": {
        "name": "Cambodia",
        "iso2": "KH",
        "short": "CB"
    },
    "ISL": {
        "name": "Iceland",
        "iso2": "IS",
        "short": "IC"
    },
    "PER": {
        "name": "Peru",
        "iso2": "PE",
        "short": "PE"
    },
    "MDG": {
        "name": "Madagascar",
        "iso2": "MG",
        "short": "MA"
    },
    "IND": {
        "name": "India",
        "iso2": "IN",
        "short": "IN"
    },
    "BRN": {
        "name": "Brunei Darussalam",
        "iso2": "BN",
        "short": "BX"
    },
    "IRN": {
        "name": "Iran (Islamic Republic of)",
        "iso2": "IR",
        "short": "IR"
    },
    "MAC": {
        "name": "China, Macao Special Administrative Region",
        "iso2": "MO",
        "short": "MC"
    },
    "ROU": {
        "name": "Romania",
        "iso2": "RO",
        "short": "RO"
    },
    "AUS": {
        "name": "Australia",
        "iso2": "AU",
        "short": "AS"
    },
    "MDA": {
        "name": "Republic of Moldova",
        "iso2": "MD",
        "short": "MD"
    },
    "IRL": {
        "name": "Ireland",
        "iso2": "IE",
        "short": "EI"
    },
    "MNE": {
        "name": "Montenegro",
        "iso2": "ME",
        "short": "MJ"
    },
    "GNQ": {
        "name": "Equatorial Guinea",
        "iso2": "GQ",
        "short": "EK"
    },
    "NPL": {
        "name": "Nepal",
        "iso2": "NP",
        "short": "NP"
    },
    "SEN": {
        "name": "Senegal",
        "iso2": "SN",
        "short": "SG"
    },
    "AZE": {
        "name": "Azerbaijan",
        "iso2": "AZ",
        "short": "AJ"
    },
    "PRI": {
        "name": "Puerto Rico",
        "iso2": "PR",
        "short": "RQ"
    },
    "TUV": {
        "name": "Tuvalu",
        "iso2": "TV",
        "short": "TV"
    },
    "NGA": {
        "name": "Nigeria",
        "iso2": "NG",
        "short": "NI"
    },
    "UGA": {
        "name": "Uganda",
        "iso2": "UG",
        "short": "UG"
    },
    "MOZ": {
        "name": "Mozambique",
        "iso2": "MZ",
        "short": "MZ"
    },
    "KEN": {
        "name": "Kenya",
        "iso2": "KE",
        "short": "KE"
    },
    "ITA": {
        "name": "Italy",
        "iso2": "IT",
        "short": "IT"
    },
    "GIN": {
        "name": "Guinea",
        "iso2": "GN",
        "short": "GV"
    },
    "SGP": {
        "name": "Singapore",
        "iso2": "SG",
        "short": "SN"
    },
    "PLW": {
        "name": "Palau",
        "iso2": "PW",
        "short": "PS"
    },
    "KNA": {
        "name": "Saint Kitts and Nevis",
        "iso2": "KN",
        "short": "SC"
    },
    "MUS": {
        "name": "Mauritius",
        "iso2": "MU",
        "short": "MP"
    },
    "TLS": {
        "name": "Timor-Leste",
        "iso2": "TL",
        "short": "TT"
    },
    "AFG": {
        "name": "Afghanistan",
        "iso2": "AF",
        "short": "AF"
    },
    "BEL": {
        "name": "Belgium",
        "iso2": "BE",
        "short": "BE"
    },
    "ZWE": {
        "name": "Zimbabwe",
        "iso2": "ZW",
        "short": "ZI"
    },
    "MYS": {
        "name": "Malaysia",
        "iso2": "MY",
        "short": "MY"
    },
    "KIR": {
        "name": "Kiribati",
        "iso2": "KI",
        "short": "KR"
    },
    "NAM": {
        "name": "Namibia",
        "iso2": "NA",
        "short": "WA"
    },
    "HTI": {
        "name": "Haiti",
        "iso2": "HT",
        "short": "HA"
    },
    "HND": {
        "name": "Honduras",
        "iso2": "HN",
        "short": "HO"
    },
    "SVN": {
        "name": "Slovenia",
        "iso2": "SI",
        "short": "SI"
    },
    "LKA": {
        "name": "Sri Lanka",
        "iso2": "LK",
        "short": "CE"
    },
    "KOR": {
        "name": "Republic of Korea",
        "iso2": "KR",
        "short": "KS"
    },
    "VUT": {
        "name": "Vanuatu",
        "iso2": "VU",
        "short": "NH"
    },
    "CHN": {
        "name": "China",
        "iso2": "CN",
        "short": "CH"
    },
    "NZL": {
        "name": "New Zealand",
        "iso2": "NZ",
        "short": "NZ"
    },
    "MRT": {
        "name": "Mauritania",
        "iso2": "MR",
        "short": "MR"
    },
    "EST": {
        "name": "Estonia",
        "iso2": "EE",
        "short": "EN"
    },
    "BIH": {
        "name": "Bosnia and Herzegovina",
        "iso2": "BA",
        "short": "BK"
    },
    "CZE": {
        "name": "Czechia",
        "iso2": "CZ",
        "short": "EZ"
    },
    "BLR": {
        "name": "Belarus",
        "iso2": "BY",
        "short": "BO"
    },
    "PAN": {
        "name": "Panama",
        "iso2": "PA",
        "short": "PM"
    },
    "KAZ": {
        "name": "Kazakhstan",
        "iso2": "KZ",
        "short": "KZ"
    },
    "ATG": {
        "name": "Antigua and Barbuda",
        "iso2": "AG",
        "short": "AC"
    },
    "ASM": {
        "name": "American Samoa",
        "iso2": "AS",
        "short": "AQ"
    },
    "NER": {
        "name": "Niger",
        "iso2": "NE",
        "short": "NG"
    },
    "SLE": {
        "name": "Sierra Leone",
        "iso2": "SL",
        "short": "SL"
    },
    "LBR": {
        "name": "Liberia",
        "iso2": "LR",
        "short": "LI"
    },
    "TUN": {
        "name": "Tunisia",
        "iso2": "TN",
        "short": "TS"
    },
    "JPN": {
        "name": "Japan",
        "iso2": "JP",
        "short": "JA"
    },
    "FRA": {
        "name": "France",
        "iso2": "FR",
        "short": "FR"
    },
    "GNB": {
        "name": "Guinea-Bissau",
        "iso2": "GW",
        "short": "PU"
    },
    "JOR": {
        "name": "Jordan",
        "iso2": "JO",
        "short": "JO"
    },
    "TJK": {
        "name": "Tajikistan",
        "iso2": "TJ",
        "short": "TI"
    },
    "FJI": {
        "name": "Fiji",
        "iso2": "FJ",
        "short": "FJ"
    },
    "TTO": {
        "name": "Trinidad and Tobago",
        "iso2": "TT",
        "short": "TD"
    },
    "ARM": {
        "name": "Armenia",
        "iso2": "AM",
        "short": "AM"
    },
    "NIC": {
        "name": "Nicaragua",
        "iso2": "NI",
        "short": "NU"
    },
    "THA": {
        "name": "Thailand",
        "iso2": "TH",
        "short": "TH"
    },
    "ECU": {
        "name": "Ecuador",
        "iso2": "EC",
        "short": "EC"
    },
    "GMB": {
        "name": "Gambia",
        "iso2": "GM",
        "short": "GA"
    },
    "BGR": {
        "name": "Bulgaria",
        "iso2": "BG",
        "short": "BU"
    },
    "GRD": {
        "name": "Grenada",
        "iso2": "GD",
        "short": "GJ"
    },
    "PRT": {
        "name": "Portugal",
        "iso2": "PT",
        "short": "PO"
    },
    "HKG": {
        "name": "China, Hong Kong Special Administrative Region",
        "iso2": "HK",
        "short": "HK"
    },
    "CHE": {
        "name": "Switzerland",
        "iso2": "CH",
        "short": "SZ"
    },
    "YEM": {
        "name": "Yemen",
        "iso2": "YE",
        "short": "YM"
    },
    "MAR": {
        "name": "Morocco",
        "iso2": "MA",
        "short": "MO"
    },
    "AUT": {
        "name": "Austria",
        "iso2": "AT",
        "short": "AU"
    },
    "HUN": {
        "name": "Hungary",
        "iso2": "HU",
        "short": "HU"
    },
    "GRC": {
        "name": "Greece",
        "iso2": "GR",
        "short": "GR"
    },
    "GTM": {
        "name": "Guatemala",
        "iso2": "GT",
        "short": "GT"
    },
    "IDN": {
        "name": "Indonesia",
        "iso2": "ID",
        "short": "ID"
    },
    "PAK": {
        "name": "Pakistan",
        "iso2": "PK",
        "short": "PK"
    },
    "DEU": {
        "name": "Germany",
        "iso2": "DE",
        "short": "GM"
    },
    "PRY": {
        "name": "Paraguay",
        "iso2": "PY",
        "short": "PA"
    },
    "SLB": {
        "name": "Solomon Islands",
        "iso2": "SB",
        "short": "BP"
    },
    "VCT": {
        "name": "Saint Vincent and the Grenadines",
        "iso2": "VC",
        "short": "VC"
    },
    "ESP": {
        "name": "Spain",
        "iso2": "ES",
        "short": "SP"
    },
    "USA": {
        "name": "United States of America",
        "iso2": "US",
        "short": "US"
    },
    "SMR": {
        "name": "San Marino",
        "iso2": "SM",
        "short": "SM"
    },
    "TON": {
        "name": "Tonga",
        "iso2": "TO",
        "short": "TN"
    },
    "OMN": {
        "name": "Oman",
        "iso2": "OM",
        "short": "MU"
    },
    "SVK": {
        "name": "Slovakia",
        "iso2": "SK",
        "short": "LO"
    },
    "GUM": {
        "name": "Guam",
        "iso2": "GU",
        "short": "GQ"
    },
    "MNG": {
        "name": "Mongolia",
        "iso2": "MN",
        "short": "MG"
    },
    "UKR": {
        "name": "Ukraine",
        "iso2": "UA",
        "short": "UP"
    },
    "JAM": {
        "name": "Jamaica",
        "iso2": "JM",
        "short": "JM"
    },
    "SOM": {
        "name": "Somalia",
        "iso2": "SO",
        "short": "SO"
    },
    "SYC": {
        "name": "Seychelles",
        "iso2": "SC",
        "short": "SE"
    },
    "KGZ": {
        "name": "Kyrgyzstan",
        "iso2": "KG",
        "short": "KG"
    },
    "GEO": {
        "name": "Georgia",
        "iso2": "GE",
        "short": "GG"
    },
    "LTU": {
        "name": "Lithuania",
        "iso2": "LT",
        "short": "LH"
    },
    "STP": {
        "name": "Sao Tome and Principe",
        "iso2": "ST",
        "short": "TP"
    },
    "LAO": {
        "name": "Lao People's Democratic Republic",
        "iso2": "LA",
        "short": "LA"
    },
    "LSO": {
        "name": "Lesotho",
        "iso2": "LS",
        "short": "LT"
    },
    "TUR": {
        "name": "Turkey",
        "iso2": "TR",
        "short": "TU"
    },
    "ALB": {
        "name": "Albania",
        "iso2": "AL",
        "short": "AL"
    },
    "IRQ": {
        "name": "Iraq",
        "iso2": "IQ",
        "short": "IZ"
    },
    "COD": {
        "name": "Democratic Republic of the Congo",
        "iso2": "CD",
        "short": "CG"
    },
    "CAN": {
        "name": "Canada",
        "iso2": "CA",
        "short": "CA"
    },
    "COG": {
        "name": "Congo",
        "iso2": "CG",
        "short": "CF"
    },
    "LBN": {
        "name": "Lebanon",
        "iso2": "LB",
        "short": "LE"
    },
    "MHL": {
        "name": "Marshall Islands",
        "iso2": "MH",
        "short": "RM"
    },
    "SWE": {
        "name": "Sweden",
        "iso2": "SE",
        "short": "SW"
    },
    "POL": {
        "name": "Poland",
        "iso2": "PL",
        "short": "PL"
    },
    "TZA": {
        "name": "United Republic of Tanzania",
        "iso2": "TZ",
        "short": "TZ"
    },
    "BHR": {
        "name": "Bahrain",
        "iso2": "BH",
        "short": "BA"
    },
    "AND": {
        "name": "Andorra",
        "iso2": "AD",
        "short": "AN"
    },
    "TKM": {
        "name": "Turkmenistan",
        "iso2": "TM",
        "short": "TX"
    },
    "DZA": {
        "name": "Algeria",
        "iso2": "DZ",
        "short": "AG"
    },
    "UZB": {
        "name": "Uzbekistan",
        "iso2": "UZ",
        "short": "UZ"
    },
    "CAF": {
        "name": "Central African Republic",
        "iso2": "CF",
        "short": "CT"
    },
    "ZAF": {
        "name": "South Africa",
        "iso2": "ZA",
        "short": "SF"
    },
    "NLD": {
        "name": "Netherlands",
        "iso2": "NL",
        "short": "NL"
    },
    "LUX": {
        "name": "Luxembourg",
        "iso2": "LU",
        "short": "LU"
    },
    "BRA": {
        "name": "Brazil",
        "iso2": "BR",
        "short": "BR"
    },
    "DMA": {
        "name": "Dominica",
        "iso2": "DM",
        "short": "DO"
    },
    "ARG": {
        "name": "Argentina",
        "iso2": "AR",
        "short": "AR"
    },
    "WSM": {
        "name": "Samoa",
        "iso2": "WS",
        "short": "WS"
    },
    "FSM": {
        "name": "Micronesia (Federated States of)",
        "iso2": "FM",
        "short": "FM"
    },
    "CYP": {
        "name": "Cyprus",
        "iso2": "CY",
        "short": "CY"
    },
    "MKD": {
        "name": "The former Yugoslav Republic of Macedonia",
        "iso2": "MK",
        "short": "MK"
    },
    "MNP": {
        "name": "Northern Mariana Islands",
        "iso2": "MP",
        "short": "CQ"
    },
    "ISR": {
        "name": "Israel",
        "iso2": "IL",
        "short": "IS"
    },
    "RUS": {
        "name": "Russian Federation",
        "iso2": "RU",
        "short": "RS"
    },
    "VNM": {
        "name": "Viet Nam",
        "iso2": "VN",
        "short": "VM"
    },
    "FIN": {
        "name": "Finland",
        "iso2": "FI",
        "short": "FI"
    },
    "SUR": {
        "name": "Suriname",
        "iso2": "SR",
        "short": "NS"
    },
    "GUY": {
        "name": "Guyana",
        "iso2": "GY",
        "short": "GY"
    },
    "CIV": {
        "name": "C te d'Ivoire",
        "iso2": "CI",
        "short": "IV"
    },
    "GAB": {
        "name": "Gabon",
        "iso2": "GA",
        "short": "GB"
    },
    "ARE": {
        "name": "United Arab Emirates",
        "iso2": "AE",
        "short": "AE"
    },
    "GBR": {
        "name": "United Kingdom of Great Britain and Northern Ireland",
        "iso2": "GB",
        "short": "UK"
    },
    "DNK": {
        "name": "Denmark",
        "iso2": "DK",
        "short": "DA"
    },
    "LCA": {
        "name": "Saint Lucia",
        "iso2": "LC",
        "short": "ST"
    },
    "CPV": {
        "name": "Cabo Verde",
        "iso2": "CV",
        "short": "CV"
    },
    "NRU": {
        "name": "Nauru",
        "iso2": "NR",
        "short": "NR"
    },
    "CHL": {
        "name": "Chile",
        "iso2": "CL",
        "short": "CI"
    },
    "MWI": {
        "name": "Malawi",
        "iso2": "MW",
        "short": "MI"
    },
    "CMR": {
        "name": "Cameroon",
        "iso2": "CM",
        "short": "CM"
    },
    "BDI": {
        "name": "Burundi",
        "iso2": "BI",
        "short": "BY"
    },
    "TGO": {
        "name": "Togo",
        "iso2": "TG",
        "short": "TO"
    },
    "MLT": {
        "name": "Malta",
        "iso2": "MT",
        "short": "MT"
    },
    "SDN": {
        "name": "Sudan",
        "iso2": "SD",
        "short": "SU"
    },
    "BLZ": {
        "name": "Belize",
        "iso2": "BZ",
        "short": "BH"
    }
}


# this is a full-list of country, just for backup
# global_codes = {
#     "AFG": {
#         "name": "Afghanistan",
#         "iso2": "AF",
#         "short": "AF"
#     },
#     "ALB": {
#         "name": "Albania",
#         "iso2": "AL",
#         "short": "AL"
#     },
#     "DZA": {
#         "name": "Algeria",
#         "iso2": "DZ",
#         "short": "AG"
#     },
#     "ASM": {
#         "name": "American Samoa",
#         "iso2": "AS",
#         "short": "AQ"
#     },
#     "AND": {
#         "name": "Andorra",
#         "iso2": "AD",
#         "short": "AN"
#     },
#     "AGO": {
#         "name": "Angola",
#         "iso2": "AO",
#         "short": "AO"
#     },
#     "AIA": {
#         "name": "Anguilla",
#         "iso2": "AI",
#         "short": "AV"
#     },
#     "ATA": {
#         "name": "Antarctica",
#         "iso2": "AQ",
#         "short": "AY"
#     },
#     "ATG": {
#         "name": "Antigua and Barbuda",
#         "iso2": "AG",
#         "short": "AC"
#     },
#     "ARG": {
#         "name": "Argentina",
#         "iso2": "AR",
#         "short": "AR"
#     },
#     "ARM": {
#         "name": "Armenia",
#         "iso2": "AM",
#         "short": "AM"
#     },
#     "ABW": {
#         "name": "Aruba",
#         "iso2": "AW",
#         "short": "AA"
#     },
#     "AUS": {
#         "name": "Australia",
#         "iso2": "AU",
#         "short": "AS"
#     },
#     "AUT": {
#         "name": "Austria",
#         "iso2": "AT",
#         "short": "AU"
#     },
#     "AZE": {
#         "name": "Azerbaijan",
#         "iso2": "AZ",
#         "short": "AJ"
#     },
#     "BHS": {
#         "name": "Bahamas",
#         "iso2": "BS",
#         "short": "BF"
#     },
#     "BHR": {
#         "name": "Bahrain",
#         "iso2": "BH",
#         "short": "BA"
#     },
#     "BGD": {
#         "name": "Bangladesh",
#         "iso2": "BD",
#         "short": "BG"
#     },
#     "BRB": {
#         "name": "Barbados",
#         "iso2": "BB",
#         "short": "BB"
#     },
#     "BLR": {
#         "name": "Belarus",
#         "iso2": "BY",
#         "short": "BO"
#     },
#     "BEL": {
#         "name": "Belgium",
#         "iso2": "BE",
#         "short": "BE"
#     },
#     "BLZ": {
#         "name": "Belize",
#         "iso2": "BZ",
#         "short": "BH"
#     },
#     "BEN": {
#         "name": "Benin",
#         "iso2": "BJ",
#         "short": "BN"
#     },
#     "BMU": {
#         "name": "Bermuda",
#         "iso2": "BM",
#         "short": "BD"
#     },
#     "BTN": {
#         "name": "Bhutan",
#         "iso2": "BT",
#         "short": "BT"
#     },
#     "BOL": {
#         "name": "Bolivia (Plurinational State of)",
#         "iso2": "BO",
#         "short": "BL"
#     },
#     "BES": {
#         "name": "Bonaire, Sint Eustatius and Saba",
#         "iso2": "BQ",
#         "short": "NL"
#     },
#     "BIH": {
#         "name": "Bosnia and Herzegovina",
#         "iso2": "BA",
#         "short": "BK"
#     },
#     "BWA": {
#         "name": "Botswana",
#         "iso2": "BW",
#         "short": "BC"
#     },
#     "BVT": {
#         "name": "Bouvet Island",
#         "iso2": "BV",
#         "short": "BV"
#     },
#     "BRA": {
#         "name": "Brazil",
#         "iso2": "BR",
#         "short": "BR"
#     },
#     "IOT": {
#         "name": "British Indian Ocean Territory",
#         "iso2": "IO",
#         "short": "IO"
#     },
#     "VGB": {
#         "name": "British Virgin Islands",
#         "iso2": "VG",
#         "short": "VI"
#     },
#     "BRN": {
#         "name": "Brunei Darussalam",
#         "iso2": "BN",
#         "short": "BX"
#     },
#     "BGR": {
#         "name": "Bulgaria",
#         "iso2": "BG",
#         "short": "BU"
#     },
#     "BFA": {
#         "name": "Burkina Faso",
#         "iso2": "BF",
#         "short": "UV"
#     },
#     "BDI": {
#         "name": "Burundi",
#         "iso2": "BI",
#         "short": "BY"
#     },
#     "CPV": {
#         "name": "Cabo Verde",
#         "iso2": "CV",
#         "short": "CV"
#     },
#     "KHM": {
#         "name": "Cambodia",
#         "iso2": "KH",
#         "short": "CB"
#     },
#     "CMR": {
#         "name": "Cameroon",
#         "iso2": "CM",
#         "short": "CM"
#     },
#     "CAN": {
#         "name": "Canada",
#         "iso2": "CA",
#         "short": "CA"
#     },
#     "CYM": {
#         "name": "Cayman Islands",
#         "iso2": "KY",
#         "short": "CJ"
#     },
#     "CAF": {
#         "name": "Central African Republic",
#         "iso2": "CF",
#         "short": "CT"
#     },
#     "TCD": {
#         "name": "Chad",
#         "iso2": "TD",
#         "short": "CD"
#     },
#     "CHL": {
#         "name": "Chile",
#         "iso2": "CL",
#         "short": "CI"
#     },
#     "CHN": {
#         "name": "China",
#         "iso2": "CN",
#         "short": "CH"
#     },
#     "HKG": {
#         "name": "China, Hong Kong Special Administrative Region",
#         "iso2": "HK",
#         "short": "HK"
#     },
#     "MAC": {
#         "name": "China, Macao Special Administrative Region",
#         "iso2": "MO",
#         "short": "MC"
#     },
#     "CXR": {
#         "name": "Christmas Island",
#         "iso2": "CX",
#         "short": "KT"
#     },
#     "CCK": {
#         "name": "Cocos (Keeling) Islands",
#         "iso2": "CC",
#         "short": "CK"
#     },
#     "COL": {
#         "name": "Colombia",
#         "iso2": "CO",
#         "short": "CO"
#     },
#     "COM": {
#         "name": "Comoros",
#         "iso2": "KM",
#         "short": "CN"
#     },
#     "COG": {
#         "name": "Congo",
#         "iso2": "CG",
#         "short": "CF"
#     },
#     "COK": {
#         "name": "Cook Islands",
#         "iso2": "CK",
#         "short": "CW"
#     },
#     "CRI": {
#         "name": "Costa Rica",
#         "iso2": "CR",
#         "short": "CS"
#     },
#     "HRV": {
#         "name": "Croatia",
#         "iso2": "HR",
#         "short": "HR"
#     },
#     "CUB": {
#         "name": "Cuba",
#         "iso2": "CU",
#         "short": "CU"
#     },
#     "CUW": {
#         "name": "Cura ao",
#         "iso2": "CW",
#         "short": "UC"
#     },
#     "CYP": {
#         "name": "Cyprus",
#         "iso2": "CY",
#         "short": "CY"
#     },
#     "CZE": {
#         "name": "Czechia",
#         "iso2": "CZ",
#         "short": "EZ"
#     },
#     "CIV": {
#         "name": "C te d'Ivoire",
#         "iso2": "CI",
#         "short": "IV"
#     },
#     "PRK": {
#         "name": "Democratic People's Republic of Korea",
#         "iso2": "KP",
#         "short": "KN"
#     },
#     "COD": {
#         "name": "Democratic Republic of the Congo",
#         "iso2": "CD",
#         "short": "CG"
#     },
#     "DNK": {
#         "name": "Denmark",
#         "iso2": "DK",
#         "short": "DA"
#     },
#     "DJI": {
#         "name": "Djibouti",
#         "iso2": "DJ",
#         "short": "DJ"
#     },
#     "DMA": {
#         "name": "Dominica",
#         "iso2": "DM",
#         "short": "DO"
#     },
#     "DOM": {
#         "name": "Dominican Republic",
#         "iso2": "DO",
#         "short": "DR"
#     },
#     "ECU": {
#         "name": "Ecuador",
#         "iso2": "EC",
#         "short": "EC"
#     },
#     "EGY": {
#         "name": "Egypt",
#         "iso2": "EG",
#         "short": "EG"
#     },
#     "SLV": {
#         "name": "El Salvador",
#         "iso2": "SV",
#         "short": "ES"
#     },
#     "GNQ": {
#         "name": "Equatorial Guinea",
#         "iso2": "GQ",
#         "short": "EK"
#     },
#     "ERI": {
#         "name": "Eritrea",
#         "iso2": "ER",
#         "short": "ER"
#     },
#     "EST": {
#         "name": "Estonia",
#         "iso2": "EE",
#         "short": "EN"
#     },
#     "ETH": {
#         "name": "Ethiopia",
#         "iso2": "ET",
#         "short": "ET"
#     },
#     "FLK": {
#         "name": "Falkland Islands (Malvinas)",
#         "iso2": "FK",
#         "short": "FK"
#     },
#     "FRO": {
#         "name": "Faroe Islands",
#         "iso2": "FO",
#         "short": "FO"
#     },
#     "FJI": {
#         "name": "Fiji",
#         "iso2": "FJ",
#         "short": "FJ"
#     },
#     "FIN": {
#         "name": "Finland",
#         "iso2": "FI",
#         "short": "FI"
#     },
#     "FRA": {
#         "name": "France",
#         "iso2": "FR",
#         "short": "FR"
#     },
#     "GUF": {
#         "name": "French Guiana",
#         "iso2": "GF",
#         "short": "FG"
#     },
#     "PYF": {
#         "name": "French Polynesia",
#         "iso2": "PF",
#         "short": "FP"
#     },
#     "ATF": {
#         "name": "French Southern Territories",
#         "iso2": "TF",
#         "short": "FS"
#     },
#     "GAB": {
#         "name": "Gabon",
#         "iso2": "GA",
#         "short": "GB"
#     },
#     "GMB": {
#         "name": "Gambia",
#         "iso2": "GM",
#         "short": "GA"
#     },
#     "GEO": {
#         "name": "Georgia",
#         "iso2": "GE",
#         "short": "GG"
#     },
#     "DEU": {
#         "name": "Germany",
#         "iso2": "DE",
#         "short": "GM"
#     },
#     "GHA": {
#         "name": "Ghana",
#         "iso2": "GH",
#         "short": "GH"
#     },
#     "GIB": {
#         "name": "Gibraltar",
#         "iso2": "GI",
#         "short": "GI"
#     },
#     "GRC": {
#         "name": "Greece",
#         "iso2": "GR",
#         "short": "GR"
#     },
#     "GRL": {
#         "name": "Greenland",
#         "iso2": "GL",
#         "short": "GL"
#     },
#     "GRD": {
#         "name": "Grenada",
#         "iso2": "GD",
#         "short": "GJ"
#     },
#     "GLP": {
#         "name": "Guadeloupe",
#         "iso2": "GP",
#         "short": "GP"
#     },
#     "GUM": {
#         "name": "Guam",
#         "iso2": "GU",
#         "short": "GQ"
#     },
#     "GTM": {
#         "name": "Guatemala",
#         "iso2": "GT",
#         "short": "GT"
#     },
#     "GGY": {
#         "name": "Guernsey",
#         "iso2": "GG",
#         "short": "GK"
#     },
#     "GIN": {
#         "name": "Guinea",
#         "iso2": "GN",
#         "short": "GV"
#     },
#     "GNB": {
#         "name": "Guinea-Bissau",
#         "iso2": "GW",
#         "short": "PU"
#     },
#     "GUY": {
#         "name": "Guyana",
#         "iso2": "GY",
#         "short": "GY"
#     },
#     "HTI": {
#         "name": "Haiti",
#         "iso2": "HT",
#         "short": "HA"
#     },
#     "HMD": {
#         "name": "Heard Island and McDonald Islands",
#         "iso2": "HM",
#         "short": "HM"
#     },
#     "VAT": {
#         "name": "Holy See",
#         "iso2": "VA",
#         "short": "VT"
#     },
#     "HND": {
#         "name": "Honduras",
#         "iso2": "HN",
#         "short": "HO"
#     },
#     "HUN": {
#         "name": "Hungary",
#         "iso2": "HU",
#         "short": "HU"
#     },
#     "ISL": {
#         "name": "Iceland",
#         "iso2": "IS",
#         "short": "IC"
#     },
#     "IND": {
#         "name": "India",
#         "iso2": "IN",
#         "short": "IN"
#     },
#     "IDN": {
#         "name": "Indonesia",
#         "iso2": "ID",
#         "short": "ID"
#     },
#     "IRN": {
#         "name": "Iran (Islamic Republic of)",
#         "iso2": "IR",
#         "short": "IR"
#     },
#     "IRQ": {
#         "name": "Iraq",
#         "iso2": "IQ",
#         "short": "IZ"
#     },
#     "IRL": {
#         "name": "Ireland",
#         "iso2": "IE",
#         "short": "EI"
#     },
#     "IMN": {
#         "name": "Isle of Man",
#         "iso2": "IM",
#         "short": "IM"
#     },
#     "ISR": {
#         "name": "Israel",
#         "iso2": "IL",
#         "short": "IS"
#     },
#     "ITA": {
#         "name": "Italy",
#         "iso2": "IT",
#         "short": "IT"
#     },
#     "JAM": {
#         "name": "Jamaica",
#         "iso2": "JM",
#         "short": "JM"
#     },
#     "JPN": {
#         "name": "Japan",
#         "iso2": "JP",
#         "short": "JA"
#     },
#     "JEY": {
#         "name": "Jersey",
#         "iso2": "JE",
#         "short": "JE"
#     },
#     "JOR": {
#         "name": "Jordan",
#         "iso2": "JO",
#         "short": "JO"
#     },
#     "KAZ": {
#         "name": "Kazakhstan",
#         "iso2": "KZ",
#         "short": "KZ"
#     },
#     "KEN": {
#         "name": "Kenya",
#         "iso2": "KE",
#         "short": "KE"
#     },
#     "KIR": {
#         "name": "Kiribati",
#         "iso2": "KI",
#         "short": "KR"
#     },
#     "KWT": {
#         "name": "Kuwait",
#         "iso2": "KW",
#         "short": "KU"
#     },
#     "KGZ": {
#         "name": "Kyrgyzstan",
#         "iso2": "KG",
#         "short": "KG"
#     },
#     "LAO": {
#         "name": "Lao People's Democratic Republic",
#         "iso2": "LA",
#         "short": "LA"
#     },
#     "LVA": {
#         "name": "Latvia",
#         "iso2": "LV",
#         "short": "LG"
#     },
#     "LBN": {
#         "name": "Lebanon",
#         "iso2": "LB",
#         "short": "LE"
#     },
#     "LSO": {
#         "name": "Lesotho",
#         "iso2": "LS",
#         "short": "LT"
#     },
#     "LBR": {
#         "name": "Liberia",
#         "iso2": "LR",
#         "short": "LI"
#     },
#     "LBY": {
#         "name": "Libya",
#         "iso2": "LY",
#         "short": "LY"
#     },
#     "LIE": {
#         "name": "Liechtenstein",
#         "iso2": "LI",
#         "short": "LS"
#     },
#     "LTU": {
#         "name": "Lithuania",
#         "iso2": "LT",
#         "short": "LH"
#     },
#     "LUX": {
#         "name": "Luxembourg",
#         "iso2": "LU",
#         "short": "LU"
#     },
#     "MDG": {
#         "name": "Madagascar",
#         "iso2": "MG",
#         "short": "MA"
#     },
#     "MWI": {
#         "name": "Malawi",
#         "iso2": "MW",
#         "short": "MI"
#     },
#     "MYS": {
#         "name": "Malaysia",
#         "iso2": "MY",
#         "short": "MY"
#     },
#     "MDV": {
#         "name": "Maldives",
#         "iso2": "MV",
#         "short": "MV"
#     },
#     "MLI": {
#         "name": "Mali",
#         "iso2": "ML",
#         "short": "ML"
#     },
#     "MLT": {
#         "name": "Malta",
#         "iso2": "MT",
#         "short": "MT"
#     },
#     "MHL": {
#         "name": "Marshall Islands",
#         "iso2": "MH",
#         "short": "RM"
#     },
#     "MTQ": {
#         "name": "Martinique",
#         "iso2": "MQ",
#         "short": "MB"
#     },
#     "MRT": {
#         "name": "Mauritania",
#         "iso2": "MR",
#         "short": "MR"
#     },
#     "MUS": {
#         "name": "Mauritius",
#         "iso2": "MU",
#         "short": "MP"
#     },
#     "MYT": {
#         "name": "Mayotte",
#         "iso2": "YT",
#         "short": "MF"
#     },
#     "MEX": {
#         "name": "Mexico",
#         "iso2": "MX",
#         "short": "MX"
#     },
#     "FSM": {
#         "name": "Micronesia (Federated States of)",
#         "iso2": "FM",
#         "short": "FM"
#     },
#     "MCO": {
#         "name": "Monaco",
#         "iso2": "MC",
#         "short": "MN"
#     },
#     "MNG": {
#         "name": "Mongolia",
#         "iso2": "MN",
#         "short": "MG"
#     },
#     "MNE": {
#         "name": "Montenegro",
#         "iso2": "ME",
#         "short": "MJ"
#     },
#     "MSR": {
#         "name": "Montserrat",
#         "iso2": "MS",
#         "short": "MH"
#     },
#     "MAR": {
#         "name": "Morocco",
#         "iso2": "MA",
#         "short": "MO"
#     },
#     "MOZ": {
#         "name": "Mozambique",
#         "iso2": "MZ",
#         "short": "MZ"
#     },
#     "MMR": {
#         "name": "Myanmar",
#         "iso2": "MM",
#         "short": "BM"
#     },
#     "NAM": {
#         "name": "Namibia",
#         "iso2": "NA",
#         "short": "WA"
#     },
#     "NRU": {
#         "name": "Nauru",
#         "iso2": "NR",
#         "short": "NR"
#     },
#     "NPL": {
#         "name": "Nepal",
#         "iso2": "NP",
#         "short": "NP"
#     },
#     "NLD": {
#         "name": "Netherlands",
#         "iso2": "NL",
#         "short": "NL"
#     },
#     "NCL": {
#         "name": "New Caledonia",
#         "iso2": "NC",
#         "short": "NC"
#     },
#     "NZL": {
#         "name": "New Zealand",
#         "iso2": "NZ",
#         "short": "NZ"
#     },
#     "NIC": {
#         "name": "Nicaragua",
#         "iso2": "NI",
#         "short": "NU"
#     },
#     "NER": {
#         "name": "Niger",
#         "iso2": "NE",
#         "short": "NG"
#     },
#     "NGA": {
#         "name": "Nigeria",
#         "iso2": "NG",
#         "short": "NI"
#     },
#     "NIU": {
#         "name": "Niue",
#         "iso2": "NU",
#         "short": "NE"
#     },
#     "NFK": {
#         "name": "Norfolk Island",
#         "iso2": "NF",
#         "short": "NF"
#     },
#     "MNP": {
#         "name": "Northern Mariana Islands",
#         "iso2": "MP",
#         "short": "CQ"
#     },
#     "NOR": {
#         "name": "Norway",
#         "iso2": "NO",
#         "short": "NO"
#     },
#     "OMN": {
#         "name": "Oman",
#         "iso2": "OM",
#         "short": "MU"
#     },
#     "PAK": {
#         "name": "Pakistan",
#         "iso2": "PK",
#         "short": "PK"
#     },
#     "PLW": {
#         "name": "Palau",
#         "iso2": "PW",
#         "short": "PS"
#     },
#     "PAN": {
#         "name": "Panama",
#         "iso2": "PA",
#         "short": "PM"
#     },
#     "PNG": {
#         "name": "Papua New Guinea",
#         "iso2": "PG",
#         "short": "PP"
#     },
#     "PRY": {
#         "name": "Paraguay",
#         "iso2": "PY",
#         "short": "PA"
#     },
#     "PER": {
#         "name": "Peru",
#         "iso2": "PE",
#         "short": "PE"
#     },
#     "PHL": {
#         "name": "Philippines",
#         "iso2": "PH",
#         "short": "RP"
#     },
#     "PCN": {
#         "name": "Pitcairn",
#         "iso2": "PN",
#         "short": "PC"
#     },
#     "POL": {
#         "name": "Poland",
#         "iso2": "PL",
#         "short": "PL"
#     },
#     "PRT": {
#         "name": "Portugal",
#         "iso2": "PT",
#         "short": "PO"
#     },
#     "PRI": {
#         "name": "Puerto Rico",
#         "iso2": "PR",
#         "short": "RQ"
#     },
#     "QAT": {
#         "name": "Qatar",
#         "iso2": "QA",
#         "short": "QA"
#     },
#     "KOR": {
#         "name": "Republic of Korea",
#         "iso2": "KR",
#         "short": "KS"
#     },
#     "MDA": {
#         "name": "Republic of Moldova",
#         "iso2": "MD",
#         "short": "MD"
#     },
#     "ROU": {
#         "name": "Romania",
#         "iso2": "RO",
#         "short": "RO"
#     },
#     "RUS": {
#         "name": "Russian Federation",
#         "iso2": "RU",
#         "short": "RS"
#     },
#     "RWA": {
#         "name": "Rwanda",
#         "iso2": "RW",
#         "short": "RW"
#     },
#     "REU": {
#         "name": "R union",
#         "iso2": "RE",
#         "short": "RE"
#     },
#     "BLM": {
#         "name": "Saint Barth lemy",
#         "iso2": "BL",
#         "short": "TB"
#     },
#     "SHN": {
#         "name": "Saint Helena",
#         "iso2": "SH",
#         "short": "SH"
#     },
#     "KNA": {
#         "name": "Saint Kitts and Nevis",
#         "iso2": "KN",
#         "short": "SC"
#     },
#     "LCA": {
#         "name": "Saint Lucia",
#         "iso2": "LC",
#         "short": "ST"
#     },
#     "MAF": {
#         "name": "Saint Martin (French Part)",
#         "iso2": "MF",
#         "short": "RN"
#     },
#     "SPM": {
#         "name": "Saint Pierre and Miquelon",
#         "iso2": "PM",
#         "short": "SB"
#     },
#     "VCT": {
#         "name": "Saint Vincent and the Grenadines",
#         "iso2": "VC",
#         "short": "VC"
#     },
#     "WSM": {
#         "name": "Samoa",
#         "iso2": "WS",
#         "short": "WS"
#     },
#     "SMR": {
#         "name": "San Marino",
#         "iso2": "SM",
#         "short": "SM"
#     },
#     "STP": {
#         "name": "Sao Tome and Principe",
#         "iso2": "ST",
#         "short": "TP"
#     },
#     "SAU": {
#         "name": "Saudi Arabia",
#         "iso2": "SA",
#         "short": "SA"
#     },
#     "SEN": {
#         "name": "Senegal",
#         "iso2": "SN",
#         "short": "SG"
#     },
#     "SYC": {
#         "name": "Seychelles",
#         "iso2": "SC",
#         "short": "SE"
#     },
#     "SLE": {
#         "name": "Sierra Leone",
#         "iso2": "SL",
#         "short": "SL"
#     },
#     "SGP": {
#         "name": "Singapore",
#         "iso2": "SG",
#         "short": "SN"
#     },
#     "SXM": {
#         "name": "Sint Maarten (Dutch part)",
#         "iso2": "SX",
#         "short": "NN"
#     },
#     "SVK": {
#         "name": "Slovakia",
#         "iso2": "SK",
#         "short": "LO"
#     },
#     "SVN": {
#         "name": "Slovenia",
#         "iso2": "SI",
#         "short": "SI"
#     },
#     "SLB": {
#         "name": "Solomon Islands",
#         "iso2": "SB",
#         "short": "BP"
#     },
#     "SOM": {
#         "name": "Somalia",
#         "iso2": "SO",
#         "short": "SO"
#     },
#     "ZAF": {
#         "name": "South Africa",
#         "iso2": "ZA",
#         "short": "SF"
#     },
#     "SGS": {
#         "name": "South Georgia and the South Sandwich Islands",
#         "iso2": "GS",
#         "short": "SX"
#     },
#     "SSD": {
#         "name": "South Sudan",
#         "iso2": "SS",
#         "short": "OD"
#     },
#     "ESP": {
#         "name": "Spain",
#         "iso2": "ES",
#         "short": "SP"
#     },
#     "LKA": {
#         "name": "Sri Lanka",
#         "iso2": "LK",
#         "short": "CE"
#     },
#     "SDN": {
#         "name": "Sudan",
#         "iso2": "SD",
#         "short": "SU"
#     },
#     "SUR": {
#         "name": "Suriname",
#         "iso2": "SR",
#         "short": "NS"
#     },
#     "SWZ": {
#         "name": "Swaziland",
#         "iso2": "SZ",
#         "short": "WZ"
#     },
#     "SWE": {
#         "name": "Sweden",
#         "iso2": "SE",
#         "short": "SW"
#     },
#     "CHE": {
#         "name": "Switzerland",
#         "iso2": "CH",
#         "short": "SZ"
#     },
#     "SYR": {
#         "name": "Syrian Arab Republic",
#         "iso2": "SY",
#         "short": "SY"
#     },
#     "TJK": {
#         "name": "Tajikistan",
#         "iso2": "TJ",
#         "short": "TI"
#     },
#     "THA": {
#         "name": "Thailand",
#         "iso2": "TH",
#         "short": "TH"
#     },
#     "MKD": {
#         "name": "The former Yugoslav Republic of Macedonia",
#         "iso2": "MK",
#         "short": "MK"
#     },
#     "TLS": {
#         "name": "Timor-Leste",
#         "iso2": "TL",
#         "short": "TT"
#     },
#     "TGO": {
#         "name": "Togo",
#         "iso2": "TG",
#         "short": "TO"
#     },
#     "TKL": {
#         "name": "Tokelau",
#         "iso2": "TK",
#         "short": "TL"
#     },
#     "TON": {
#         "name": "Tonga",
#         "iso2": "TO",
#         "short": "TN"
#     },
#     "TTO": {
#         "name": "Trinidad and Tobago",
#         "iso2": "TT",
#         "short": "TD"
#     },
#     "TUN": {
#         "name": "Tunisia",
#         "iso2": "TN",
#         "short": "TS"
#     },
#     "TUR": {
#         "name": "Turkey",
#         "iso2": "TR",
#         "short": "TU"
#     },
#     "TKM": {
#         "name": "Turkmenistan",
#         "iso2": "TM",
#         "short": "TX"
#     },
#     "TCA": {
#         "name": "Turks and Caicos Islands",
#         "iso2": "TC",
#         "short": "TK"
#     },
#     "TUV": {
#         "name": "Tuvalu",
#         "iso2": "TV",
#         "short": "TV"
#     },
#     "UGA": {
#         "name": "Uganda",
#         "iso2": "UG",
#         "short": "UG"
#     },
#     "UKR": {
#         "name": "Ukraine",
#         "iso2": "UA",
#         "short": "UP"
#     },
#     "ARE": {
#         "name": "United Arab Emirates",
#         "iso2": "AE",
#         "short": "AE"
#     },
#     "GBR": {
#         "name": "United Kingdom of Great Britain and Northern Ireland",
#         "iso2": "GB",
#         "short": "UK"
#     },
#     "TZA": {
#         "name": "United Republic of Tanzania",
#         "iso2": "TZ",
#         "short": "TZ"
#     },
#     "VIR": {
#         "name": "United States Virgin Islands",
#         "iso2": "VI",
#         "short": "VQ"
#     },
#     "USA": {
#         "name": "United States of America",
#         "iso2": "US",
#         "short": "US"
#     },
#     "URY": {
#         "name": "Uruguay",
#         "iso2": "UY",
#         "short": "UY"
#     },
#     "UZB": {
#         "name": "Uzbekistan",
#         "iso2": "UZ",
#         "short": "UZ"
#     },
#     "VUT": {
#         "name": "Vanuatu",
#         "iso2": "VU",
#         "short": "NH"
#     },
#     "VEN": {
#         "name": "Venezuela (Bolivarian Republic of)",
#         "iso2": "VE",
#         "short": "VE"
#     },
#     "VNM": {
#         "name": "Viet Nam",
#         "iso2": "VN",
#         "short": "VM"
#     },
#     "WLF": {
#         "name": "Wallis and Futuna Islands",
#         "iso2": "WF",
#         "short": "WF"
#     },
#     "ESH": {
#         "name": "Western Sahara",
#         "iso2": "EH",
#         "short": "WI"
#     },
#     "YEM": {
#         "name": "Yemen",
#         "iso2": "YE",
#         "short": "YM"
#     },
#     "ZMB": {
#         "name": "Zambia",
#         "iso2": "ZM",
#         "short": "ZA"
#     },
#     "ZWE": {
#         "name": "Zimbabwe",
#         "iso2": "ZW",
#         "short": "ZI"
#     }
# }