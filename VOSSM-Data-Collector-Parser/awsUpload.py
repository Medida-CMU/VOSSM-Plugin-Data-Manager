
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import os
import sys
import time

project_root = os.environ.get('vossm_root')

conn = S3Connection(os.environ.get('access_key'), os.environ.get('secret_access_key'))
bucket = conn.get_bucket('vossm-datastore')

while True:
	command = "boto-rsync -a " + os.environ.get('access_key') + " -s " + os.environ.get('secret_access_key') + " s3://vossm-datastore/RMonitorData "+ project_root +"/raw_data/RMonitorData"
	os.system(command)
	command = "boto-rsync -a " + os.environ.get('access_key') + " -s " + os.environ.get('secret_access_key') + " s3://vossm-datastore/ShellMonitorData "+ project_root +"/raw_data/ShellMonitorData"
	os.system(command)
	time.sleep(60) 