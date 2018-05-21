import csv, json

def csv_to_list(path):
    # convert csv file to a list
    try:
        with open(path, 'r') as csv_file:
            csv_data = csv.reader(csv_file)
            csv_list = list(csv_data)
    except FileNotFoundError:
        print(path, 'not found')
        return []
    return csv_list


def get_col(title, title_list):
    col = title_list.index(title)
    print(title, ' = ', col)
    return col


def write_to_my_json(my_dict):
    my_json = json.dumps(my_dict)
    with open('./my_json.json', 'w+') as json_file:
        json_file.write(my_json)


csv_list = csv_to_list('./country-codes.csv')


title_list = csv_list[0]
key_col = get_col('ISO3166-1-Alpha-3', title_list)
name_col = get_col('official_name_en', title_list)
short_col = get_col('FIPS', title_list)


content_list = csv_list[2:]
my_dict = dict()
for row in content_list:
    key = row[key_col]
    value_dict = dict()
    name = row[name_col]
    short = row[short_col]
    if len(short) != 2: # discart any country do not has 2-letter short code
        continue
    value_dict['name'] = name
    value_dict['short'] = short
    my_dict[key] = value_dict.copy()
    # print(key, name, short)

print(my_dict)
write_to_my_json(my_dict)