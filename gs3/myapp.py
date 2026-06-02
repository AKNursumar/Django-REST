import requests
import json

URL = 'http://127.0.0.1:8000/student_api/'


# Read Data
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)

# get_data()

# create data
def post_data():
    data = {
        'name': 'Ravi',
        'roll':104,
        'city':'Dhanbad'
    }

    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)

# post_data()

# Updata Data
def update_data():
    data = {
        'id':4,
        'name': 'Rohit',
        'city':'Gondal'
    }

    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)

# update_data()

#
# Deleting Data
def delete_data():
    data = { 'id': 3 }
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)

delete_data()