# Parse.py parses the json data and writes them to DB.
# Once written, the file is moved to parsed_db folder

import json
import os
import shutil
from pprint import pprint
from pymongo import MongoClient
client = MongoClient();
db = client['VOSSM'];
collection = db['raw_data']
def parseFile(filename):
 data = []
 with open(filename) as f:
    for line in f:
        #data.append(json.loads(line))
	data = json.loads(line)
	new_json = json.loads(data[0], object_hook=remove_dot_key)
	collection.insert(new_json)
	print(new_json)

 # src = "raw_data/"
 # dst = "parsed_data/"
 # for file in os.listdir(src):
 #    print file 
 #    src_file = os.path.join(src, file)
 #    dst_file = os.path.join(dst, file)
 #    shutil.move(src_file, dst_file)
 return;


def remove_dot_key(obj):
    for key in obj.keys():
        new_key = key.replace(".","_")
        if new_key != key:
            obj[new_key] = obj[key]
            del obj[key]
    return obj


#pprint(data[1]);