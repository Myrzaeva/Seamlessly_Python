def extract_fullname_as_string(list_of_dictionaries):
    return list(map(lambda e : "{} {}".format(e['first'],e['last']),list_of_dictionaries))


names = [{'first': 'Jay', 'last': 'Myrzaeva'}, {'first': 'Bora', 'last': 'Zhol'}]
print(extract_fullname_as_string(names))