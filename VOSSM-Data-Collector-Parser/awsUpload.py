
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import os

print os.environ.get('access_key')
print os.environ.get('secret_access_key')

import sys
import time
conn = S3Connection(os.environ.get('access_key'), os.environ.get('secret_access_key'))
bucket = conn.get_bucket('vossm-datastore')
#aws s3 sync s3://vossm-datastore .
while True:
	command = "boto-rsync -a " + os.environ.get('access_key') + " -s " + os.environ.get('secret_access_key') + " s3://vossm-datastore/RMonitorData raw_data/RMonitorData"
	os.system(command)
	command = "boto-rsync -a " + os.environ.get('access_key') + " -s " + os.environ.get('secret_access_key') + " s3://vossm-datastore/ShellMonitorData raw_data/ShellMonitorData"
	os.system(command)
	time.sleep(60) 
# rs = bucket.list()

# for key in rs:
#    print key.name
   
# key = bucket.get_key("preethi.txt")
# key.get_contents_to_filename('/home/preethibaskar/Project/test.txt')