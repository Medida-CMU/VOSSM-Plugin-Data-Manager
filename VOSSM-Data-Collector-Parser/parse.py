# Parse.py parses the json data and writes them to DB.
# Once written, the file is moved to parsed_db folder
import time
import json
import os
import shutil
from pprint import pprint
from pymongo import MongoClient
client = MongoClient();
db = client['VOSSM'];
collection = db['raw_data']
parsed_collection = db['parsed_data']
def parseFile(filename):
 data = []
 selected_data = {}
 with open(filename) as f:
    for line in f:
        #data.append(json.loads(line))

	data = json.loads(line)
	new_json = json.loads(data[0], object_hook=remove_dot_key)
	selected_data['version'] =new_json['scimapInfoVersion']
	selected_data['hardware'] =new_json['platform']['hardware']
	selected_data['system'] = new_json['platform']['system']
	selected_data['user'] = new_json['user']
	selected_data['start_time'] = new_json['startTime']
	selected_data['end_time'] = new_json['endTime']
	for key in new_json['pkgT']:
		selected_data['_id'] = time.time()
		selected_data['package'] = key
		collection.insert(selected_data)
	print(selected_data)
	aggregateData()
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

def aggregateData():
	result = collection.aggregate([{"$group": {"_id" : 
												{'package': "$package",
												 'version' : "$version",
												 'hardware' : "$hardware", 
												 'system' : "$system"
												}, 
											"occurences": {"$sum": 1}
											}},
											{"$out" : "parsed_data"}
								 ])

#pprint(data[1]);