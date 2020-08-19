



def extract_full_name(li_dic):
    return {c.get('first'): c.get('last') for c in li_dic}




names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names))
