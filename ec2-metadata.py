import requests
import json

def fn(key):
    url = 'http://169.254.169.254/latest/meta-data/' + key
    val = requests.get(url)
    val = val.content.decode("utf-8").replace('/','')
    if "\n" in val:
        val = val.splitlines()
    return val

def dict_to_json(dict):
    return json.dumps(dict, indent = 4)

response = requests.get('http://169.254.169.254/latest/meta-data')
s = response.content.decode("utf-8").replace('/','')
keys = s.splitlines( )
d1 = {}
for key in keys:
    d1[key] = fn(key)
print(dict_to_json(d1))


# Query a particular data key from instance metada
data_key = input("please enter data key to query:")
d2 = {}
d2[data_key] = fn(data_key)
print(dict_to_json(d2))
