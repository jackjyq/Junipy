
############################# print control #############################
DEBUG_MODE = False   # True: print as much information False: default
SILENT_MODE = False  # True: print as less information False: default

########################## local configuration ##########################
# files inside tmp folder will be ignored by Git
ZIP_PATH = './tmp/' # zip file will be download here
CSV_PATH = './tmp/' # csv file will be unzip here
GIF_PATH = './tmp/' # gif file will be download here

# flag cache folder
FLAG_CACHE = './static/'   # used to store retrieved flag image

# a picture used when no flag can be found
NON_FLAG = './static/default_flag.gif'     


########################### mlab configuration ##########################
# database for debug
# DB_URL = "mongodb://junipy:comp9321@ds217350.mlab.com:17350/junipy_debug"
# database for deploy
DB_URL = "mongodb://junipy:comp9321@ds143907.mlab.com:43907/junipy_deploy"

# database collections, used in query(col=database collection)
OVERVIEW = 1
INDICATOR = 2
FLAG = 3

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
        "short": "AF"
    },
    "ALA": {
        "name": "Åland Islands",
        "short": "AX"
    },
    "ALB": {
        "name": "Albania",
        "short": "AL"
    },
    "DZA": {
        "name": "Algeria",
        "short": "DZ"
    },
    "ASM": {
        "name": "American Samoa",
        "short": "AS"
    },
    "AND": {
        "name": "Andorra",
        "short": "AD"
    },
    "AGO": {
        "name": "Angola",
        "short": "AO"
    },
    "AIA": {
        "name": "Anguilla",
        "short": "AI"
    },
    "ATA": {
        "name": "Antarctica",
        "short": "AQ"
    },
    "ATG": {
        "name": "Antigua and Barbuda",
        "short": "AG"
    },
    "ARG": {
        "name": "Argentina",
        "short": "AR"
    },
    "ARM": {
        "name": "Armenia",
        "short": "AM"
    },
    "ABW": {
        "name": "Aruba",
        "short": "AW"
    },
    "AUS": {
        "name": "Australia",
        "short": "AU"
    },
    "AUT": {
        "name": "Austria",
        "short": "AT"
    },
    "AZE": {
        "name": "Azerbaijan",
        "short": "AZ"
    },
    "BHS": {
        "name": "Bahamas",
        "short": "BS"
    },
    "BHR": {
        "name": "Bahrain",
        "short": "BH"
    },
    "BGD": {
        "name": "Bangladesh",
        "short": "BD"
    },
    "BRB": {
        "name": "Barbados",
        "short": "BB"
    },
    "BLR": {
        "name": "Belarus",
        "short": "BY"
    },
    "BEL": {
        "name": "Belgium",
        "short": "BE"
    },
    "BLZ": {
        "name": "Belize",
        "short": "BZ"
    },
    "BEN": {
        "name": "Benin",
        "short": "BJ"
    },
    "BMU": {
        "name": "Bermuda",
        "short": "BM"
    },
    "BTN": {
        "name": "Bhutan",
        "short": "BT"
    },
    "BOL": {
        "name": "Bolivia (Plurinational State of)",
        "short": "BO"
    },
    "BES": {
        "name": "Bonaire, Sint Eustatius and Saba",
        "short": "BQ"
    },
    "BIH": {
        "name": "Bosnia and Herzegovina",
        "short": "BA"
    },
    "BWA": {
        "name": "Botswana",
        "short": "BW"
    },
    "BVT": {
        "name": "Bouvet Island",
        "short": "BV"
    },
    "BRA": {
        "name": "Brazil",
        "short": "BR"
    },
    "IOT": {
        "name": "British Indian Ocean Territory",
        "short": "IO"
    },
    "BRN": {
        "name": "Brunei Darussalam",
        "short": "BN"
    },
    "BGR": {
        "name": "Bulgaria",
        "short": "BG"
    },
    "BFA": {
        "name": "Burkina Faso",
        "short": "BF"
    },
    "BDI": {
        "name": "Burundi",
        "short": "BI"
    },
    "CPV": {
        "name": "Cabo Verde",
        "short": "CV"
    },
    "KHM": {
        "name": "Cambodia",
        "short": "KH"
    },
    "CMR": {
        "name": "Cameroon",
        "short": "CM"
    },
    "CAN": {
        "name": "Canada",
        "short": "CA"
    },
    "CYM": {
        "name": "Cayman Islands",
        "short": "KY"
    },
    "CAF": {
        "name": "Central African Republic",
        "short": "CF"
    },
    "TCD": {
        "name": "Chad",
        "short": "TD"
    },
    "CHL": {
        "name": "Chile",
        "short": "CL"
    },
    "CHN": {
        "name": "China",
        "short": "CN"
    },
    "CXR": {
        "name": "Christmas Island",
        "short": "CX"
    },
    "CCK": {
        "name": "Cocos (Keeling) Islands",
        "short": "CC"
    },
    "COL": {
        "name": "Colombia",
        "short": "CO"
    },
    "COM": {
        "name": "Comoros",
        "short": "KM"
    },
    "COG": {
        "name": "Congo",
        "short": "CG"
    },
    "COD": {
        "name": "Congo (Democratic Republic of the)",
        "short": "CD"
    },
    "COK": {
        "name": "Cook Islands",
        "short": "CK"
    },
    "CRI": {
        "name": "Costa Rica",
        "short": "CR"
    },
    "CIV": {
        "name": "Côte d'Ivoire",
        "short": "CI"
    },
    "HRV": {
        "name": "Croatia",
        "short": "HR"
    },
    "CUB": {
        "name": "Cuba",
        "short": "CU"
    },
    "CUW": {
        "name": "Curaçao",
        "short": "CW"
    },
    "CYP": {
        "name": "Cyprus",
        "short": "CY"
    },
    "CZE": {
        "name": "Czechia",
        "short": "CZ"
    },
    "DNK": {
        "name": "Denmark",
        "short": "DK"
    },
    "DJI": {
        "name": "Djibouti",
        "short": "DJ"
    },
    "DMA": {
        "name": "Dominica",
        "short": "DM"
    },
    "DOM": {
        "name": "Dominican Republic",
        "short": "DO"
    },
    "ECU": {
        "name": "Ecuador",
        "short": "EC"
    },
    "EGY": {
        "name": "Egypt",
        "short": "EG"
    },
    "SLV": {
        "name": "El Salvador",
        "short": "SV"
    },
    "GNQ": {
        "name": "Equatorial Guinea",
        "short": "GQ"
    },
    "ERI": {
        "name": "Eritrea",
        "short": "ER"
    },
    "EST": {
        "name": "Estonia",
        "short": "EE"
    },
    "ETH": {
        "name": "Ethiopia",
        "short": "ET"
    },
    "FLK": {
        "name": "Falkland Islands (Malvinas)",
        "short": "FK"
    },
    "FRO": {
        "name": "Faroe Islands",
        "short": "FO"
    },
    "FJI": {
        "name": "Fiji",
        "short": "FJ"
    },
    "FIN": {
        "name": "Finland",
        "short": "FI"
    },
    "FRA": {
        "name": "France",
        "short": "FR"
    },
    "GUF": {
        "name": "French Guiana",
        "short": "GF"
    },
    "PYF": {
        "name": "French Polynesia",
        "short": "PF"
    },
    "ATF": {
        "name": "French Southern Territories",
        "short": "TF"
    },
    "GAB": {
        "name": "Gabon",
        "short": "GA"
    },
    "GMB": {
        "name": "Gambia",
        "short": "GM"
    },
    "GEO": {
        "name": "Georgia",
        "short": "GE"
    },
    "DEU": {
        "name": "Germany",
        "short": "DE"
    },
    "GHA": {
        "name": "Ghana",
        "short": "GH"
    },
    "GIB": {
        "name": "Gibraltar",
        "short": "GI"
    },
    "GRC": {
        "name": "Greece",
        "short": "GR"
    },
    "GRL": {
        "name": "Greenland",
        "short": "GL"
    },
    "GRD": {
        "name": "Grenada",
        "short": "GD"
    },
    "GLP": {
        "name": "Guadeloupe",
        "short": "GP"
    },
    "GUM": {
        "name": "Guam",
        "short": "GU"
    },
    "GTM": {
        "name": "Guatemala",
        "short": "GT"
    },
    "GGY": {
        "name": "Guernsey",
        "short": "GG"
    },
    "GIN": {
        "name": "Guinea",
        "short": "GN"
    },
    "GNB": {
        "name": "Guinea-Bissau",
        "short": "GW"
    },
    "GUY": {
        "name": "Guyana",
        "short": "GY"
    },
    "HTI": {
        "name": "Haiti",
        "short": "HT"
    },
    "HMD": {
        "name": "Heard Island and McDonald Islands",
        "short": "HM"
    },
    "VAT": {
        "name": "Holy See",
        "short": "VA"
    },
    "HND": {
        "name": "Honduras",
        "short": "HN"
    },
    "HKG": {
        "name": "Hong Kong",
        "short": "HK"
    },
    "HUN": {
        "name": "Hungary",
        "short": "HU"
    },
    "ISL": {
        "name": "Iceland",
        "short": "IS"
    },
    "IND": {
        "name": "India",
        "short": "IN"
    },
    "IDN": {
        "name": "Indonesia",
        "short": "ID"
    },
    "IRN": {
        "name": "Iran (Islamic Republic of)",
        "short": "IR"
    },
    "IRQ": {
        "name": "Iraq",
        "short": "IQ"
    },
    "IRL": {
        "name": "Ireland",
        "short": "IE"
    },
    "IMN": {
        "name": "Isle of Man",
        "short": "IM"
    },
    "ISR": {
        "name": "Israel",
        "short": "IL"
    },
    "ITA": {
        "name": "Italy",
        "short": "IT"
    },
    "JAM": {
        "name": "Jamaica",
        "short": "JM"
    },
    "JPN": {
        "name": "Japan",
        "short": "JP"
    },
    "JEY": {
        "name": "Jersey",
        "short": "JE"
    },
    "JOR": {
        "name": "Jordan",
        "short": "JO"
    },
    "KAZ": {
        "name": "Kazakhstan",
        "short": "KZ"
    },
    "KEN": {
        "name": "Kenya",
        "short": "KE"
    },
    "KIR": {
        "name": "Kiribati",
        "short": "KI"
    },
    "PRK": {
        "name": "Korea (Democratic People's Republic of)",
        "short": "KP"
    },
    "KOR": {
        "name": "Korea (Republic of)",
        "short": "KR"
    },
    "KWT": {
        "name": "Kuwait",
        "short": "KW"
    },
    "KGZ": {
        "name": "Kyrgyzstan",
        "short": "KG"
    },
    "LAO": {
        "name": "Lao People's Democratic Republic",
        "short": "LA"
    },
    "LVA": {
        "name": "Latvia",
        "short": "LV"
    },
    "LBN": {
        "name": "Lebanon",
        "short": "LB"
    },
    "LSO": {
        "name": "Lesotho",
        "short": "LS"
    },
    "LBR": {
        "name": "Liberia",
        "short": "LR"
    },
    "LBY": {
        "name": "Libya",
        "short": "LY"
    },
    "LIE": {
        "name": "Liechtenstein",
        "short": "LI"
    },
    "LTU": {
        "name": "Lithuania",
        "short": "LT"
    },
    "LUX": {
        "name": "Luxembourg",
        "short": "LU"
    },
    "MAC": {
        "name": "Macao",
        "short": "MO"
    },
    "MKD": {
        "name": "Macedonia (the former Yugoslav Republic of)",
        "short": "MK"
    },
    "MDG": {
        "name": "Madagascar",
        "short": "MG"
    },
    "MWI": {
        "name": "Malawi",
        "short": "MW"
    },
    "MYS": {
        "name": "Malaysia",
        "short": "MY"
    },
    "MDV": {
        "name": "Maldives",
        "short": "MV"
    },
    "MLI": {
        "name": "Mali",
        "short": "ML"
    },
    "MLT": {
        "name": "Malta",
        "short": "MT"
    },
    "MHL": {
        "name": "Marshall Islands",
        "short": "MH"
    },
    "MTQ": {
        "name": "Martinique",
        "short": "MQ"
    },
    "MRT": {
        "name": "Mauritania",
        "short": "MR"
    },
    "MUS": {
        "name": "Mauritius",
        "short": "MU"
    },
    "MYT": {
        "name": "Mayotte",
        "short": "YT"
    },
    "MEX": {
        "name": "Mexico",
        "short": "MX"
    },
    "FSM": {
        "name": "Micronesia (FederatedStates of)",
        "short": "FM"
    },
    "MDA": {
        "name": "Moldova (Republic of)",
        "short": "MD"
    },
    "MCO": {
        "name": "Monaco",
        "short": "MC"
    },
    "MNG": {
        "name": "Mongolia",
        "short": "MN"
    },
    "MNE": {
        "name": "Montenegro",
        "short": "ME"
    },
    "MSR": {
        "name": "Montserrat",
        "short": "MS"
    },
    "MAR": {
        "name": "Morocco",
        "short": "MA"
    },
    "MOZ": {
        "name": "Mozambique",
        "short": "MZ"
    },
    "MMR": {
        "name": "Myanmar",
        "short": "MM"
    },
    "NAM": {
        "name": "Namibia",
        "short": "NA"
    },
    "NRU": {
        "name": "Nauru",
        "short": "NR"
    },
    "NPL": {
        "name": "Nepal",
        "short": "NP"
    },
    "NLD": {
        "name": "Netherlands",
        "short": "NL"
    },
    "NCL": {
        "name": "New Caledonia",
        "short": "NC"
    },
    "NZL": {
        "name": "New Zealand",
        "short": "NZ"
    },
    "NIC": {
        "name": "Nicaragua",
        "short": "NI"
    },
    "NER": {
        "name": "Niger",
        "short": "NE"
    },
    "NGA": {
        "name": "Nigeria",
        "short": "NG"
    },
    "NIU": {
        "name": "Niue",
        "short": "NU"
    },
    "NFK": {
        "name": "Norfolk Island",
        "short": "NF"
    },
    "MNP": {
        "name": "Northern Mariana Islands",
        "short": "MP"
    },
    "NOR": {
        "name": "Norway",
        "short": "NO"
    },
    "OMN": {
        "name": "Oman",
        "short": "OM"
    },
    "PAK": {
        "name": "Pakistan",
        "short": "PK"
    },
    "PLW": {
        "name": "Palau",
        "short": "PW"
    },
    "PSE": {
        "name": "Palestine, State of",
        "short": "PS"
    },
    "PAN": {
        "name": "Panama",
        "short": "PA"
    },
    "PNG": {
        "name": "Papua New Guinea",
        "short": "PG"
    },
    "PRY": {
        "name": "Paraguay",
        "short": "PY"
    },
    "PER": {
        "name": "Peru",
        "short": "PE"
    },
    "PHL": {
        "name": "Philippines",
        "short": "PH"
    },
    "PCN": {
        "name": "Pitcairn",
        "short": "PN"
    },
    "POL": {
        "name": "Poland",
        "short": "PL"
    },
    "PRT": {
        "name": "Portugal",
        "short": "PT"
    },
    "PRI": {
        "name": "Puerto Rico",
        "short": "PR"
    },
    "QAT": {
        "name": "Qatar",
        "short": "QA"
    },
    "REU": {
        "name": "Réunion",
        "short": "RE"
    },
    "ROU": {
        "name": "Romania",
        "short": "RO"
    },
    "RUS": {
        "name": "Russian Federation",
        "short": "RU"
    },
    "RWA": {
        "name": "Rwanda",
        "short": "RW"
    },
    "BLM": {
        "name": "Saint Barthélemy",
        "short": "BL"
    },
    "SHN": {
        "name": "Saint Helena, Ascension and Tristan da Cunha",
        "short": "SH"
    },
    "KNA": {
        "name": "Saint Kitts and Nevis",
        "short": "KN"
    },
    "LCA": {
        "name": "Saint Lucia",
        "short": "LC"
    },
    "MAF": {
        "name": "Saint Martin (French part)",
        "short": "MF"
    },
    "SPM": {
        "name": "Saint Pierre and Miquelon",
        "short": "PM"
    },
    "VCT": {
        "name": "Saint Vincent andthe Grenadines",
        "short": "VC"
    },
    "WSM": {
        "name": "Samoa",
        "short": "WS"
    },
    "SMR": {
        "name": "San Marino",
        "short": "SM"
    },
    "STP": {
        "name": "Sao Tome and Principe",
        "short": "ST"
    },
    "SAU": {
        "name": "Saudi Arabia",
        "short": "SA"
    },
    "SEN": {
        "name": "Senegal",
        "short": "SN"
    },
    "SRB": {
        "name": "Serbia",
        "short": "RS"
    },
    "SYC": {
        "name": "Seychelles",
        "short": "SC"
    },
    "SLE": {
        "name": "Sierra Leone",
        "short": "SL"
    },
    "SGP": {
        "name": "Singapore",
        "short": "SG"
    },
    "SXM": {
        "name": "Sint Maarten (Dutch part)",
        "short": "SX"
    },
    "SVK": {
        "name": "Slovakia",
        "short": "SK"
    },
    "SVN": {
        "name": "Slovenia",
        "short": "SI"
    },
    "SLB": {
        "name": "Solomon Islands",
        "short": "SB"
    },
    "SOM": {
        "name": "Somalia",
        "short": "SO"
    },
    "ZAF": {
        "name": "South Africa",
        "short": "ZA"
    },
    "SGS": {
        "name": "South Georgia and the South Sandwich Islands",
        "short": "GS"
    },
    "SSD": {
        "name": "South Sudan",
        "short": "SS"
    },
    "ESP": {
        "name": "Spain",
        "short": "ES"
    },
    "LKA": {
        "name": "Sri Lanka",
        "short": "LK"
    },
    "SDN": {
        "name": "Sudan",
        "short": "SD"
    },
    "SUR": {
        "name": "Suriname",
        "short": "SR"
    },
    "SJM": {
        "name": "Svalbard and Jan Mayen",
        "short": "SJ"
    },
    "SWZ": {
        "name": "Swaziland",
        "short": "SZ"
    },
    "SWE": {
        "name": "Sweden",
        "short": "SE"
    },
    "CHE": {
        "name": "Switzerland",
        "short": "CH"
    },
    "SYR": {
        "name": "Syrian Arab Republic",
        "short": "SY"
    },
    "TWN": {
        "name": "Taiwan, Province of China",
        "short": "TW"
    },
    "TJK": {
        "name": "Tajikistan",
        "short": "TJ"
    },
    "TZA": {
        "name": "Tanzania, United Republic of",
        "short": "TZ"
    },
    "THA": {
        "name": "Thailand",
        "short": "TH"
    },
    "TLS": {
        "name": "Timor-Leste",
        "short": "TL"
    },
    "TGO": {
        "name": "Togo",
        "short": "TG"
    },
    "TKL": {
        "name": "Tokelau",
        "short": "TK"
    },
    "TON": {
        "name": "Tonga",
        "short": "TO"
    },
    "TTO": {
        "name": "Trinidad and Tobago",
        "short": "TT"
    },
    "TUN": {
        "name": "Tunisia",
        "short": "TN"
    },
    "TUR": {
        "name": "Turkey",
        "short": "TR"
    },
    "TKM": {
        "name": "Turkmenistan",
        "short": "TM"
    },
    "TCA": {
        "name": "Turks and Caicos Islands",
        "short": "TC"
    },
    "TUV": {
        "name": "Tuvalu",
        "short": "TV"
    },
    "UGA": {
        "name": "Uganda",
        "short": "UG"
    },
    "UKR": {
        "name": "Ukraine",
        "short": "UA"
    },
    "ARE": {
        "name": "United Arab Emirates",
        "short": "AE"
    },
    "GBR": {
        "name": "United Kingdom of Great Britain and Northern Ireland",
        "short": "GB"
    },
    "USA": {
        "name": "United States of America",
        "short": "US"
    },
    "UMI": {
        "name": "United States Minor Outlying Islands",
        "short": "UM"
    },
    "URY": {
        "name": "Uruguay",
        "short": "UY"
    },
    "UZB": {
        "name": "Uzbekistan",
        "short": "UZ"
    },
    "VUT": {
        "name": "Vanuatu",
        "short": "VU"
    },
    "VEN": {
        "name": "Venezuela (Bolivarian Republic of)",
        "short": "VE"
    },
    "VNM": {
        "name": "Viet Nam",
        "short": "VN"
    },
    "VGB": {
        "name": "Virgin Islands (British)",
        "short": "VG"
    },
    "VIR": {
        "name": "Virgin Islands (U.S.)",
        "short": "VI"
    },
    "WLF": {
        "name": "Wallis and Futuna",
        "short": "WF"
    },
    "ESH": {
        "name": "Western Sahara",
        "short": "EH"
    },
    "YEM": {
        "name": "Yemen",
        "short": "YE"
    },
    "ZMB": {
        "name": "Zambia",
        "short": "ZM"
    },
    "ZWE": {
        "name": "Zimbabwe",
        "short": "ZW"
    }
}