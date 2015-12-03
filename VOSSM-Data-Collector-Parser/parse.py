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
			data = json.loads(line)
			collection.insert(data)

		project_root = os.environ.get('vossm_root')
		src = project_root + "/raw_data/"
		dst = project_root + "/parsed_data/"

	for file in os.listdir(src):
		print file 
		src_file = os.path.join(src, file)
		dst_file = os.path.join(dst, file)
		shutil.move(src_file, dst_file)
	return;
