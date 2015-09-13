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
	collection.insert(data)

 src = "/home/preethibaskar/raw_data/"
 dst = "/home/preethibaskar/parsed_data/"
 for file in os.listdir(src):
    print file 
    src_file = os.path.join(src, file)
    dst_file = os.path.join(dst, file)
    shutil.move(src_file, dst_file)
 pprint(data);
 return;
#pprint(data[1]);
