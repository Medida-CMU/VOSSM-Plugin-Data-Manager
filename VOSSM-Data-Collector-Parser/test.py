import unittest
from parse import parseFile
import watchdir
import mongoengine
import os
from subprocess import check_output

class SimpleTest(unittest.TestCase):

	def test_sample_R(self):
		val = parseFile("/home/preethibaskar/Documents/Data/raw_data/RMonitorData/data_1446431444.json")
		self.assertEqual(200,val)

	def test_sample_unix(self):
		val = parseFile("/home/preethibaskar/Documents/Data/raw_data/ShellMonitorData/ShellData_1449473904003189615.log")
		self.assertEqual(200,val)

	def test_watchdog(self):
		os.system('export vossm_root=/home/preethibaskar/Documents/Data')
		os.system('export access_key=')
		os.system('export secret_access_key=')
		os.system('python watchdir.py')
		val = os.system('cp /home/preethibaskar/Documents/Data/raw_data/ShellMonitorData/ShellData_1449473904003189615.log /home/preethibaskar/Documents/Data/raw_data/ShellMonitorData/ShellData_1449473904003189615_new.log')
		return
	def test_awsUpload(self):
		os.system('rm -rf /home/preethibaskar/Documents/Data/raw_data/RMonitorData/data_1446431444.json')
		os.system('export vossm_root=/home/preethibaskar/Documents/Data')
		os.system('export access_key=')
		os.system('export secret_access_key=')
		os.system('python awsUpload.py')


if __name__ == '__main__':
    unittest.main()