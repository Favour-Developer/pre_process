"""
Converting excel to this type

"ids":[
    "17112067" : {
        "Name" : "Ritik Gupta",
        "Room_NO" : "A122",
        "Hostel" : "Rajiv"
    }
]
"""
import json
db = open('data.json')
with db as data_file:
    data = json.load(data_file)
    dic = {}
    for v in data['Student']:
        dic[v['Enro']] = v
with open('converted_data.json',"w") as outfile:
    json.dump(dic, outfile, indent=4)
