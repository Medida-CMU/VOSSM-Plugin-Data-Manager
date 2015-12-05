import csv
import json
from pymongo import MongoClient
from bs4 import BeautifulSoup
import urllib2

client = MongoClient();
db = client['VOSSM'];
collection = db['package_details']

def get_name_company(packageName):

	package_page = urllib2.urlopen("https://cran.r-project.org/web/packages/"+ packageName +"/index.html")
	package_data = BeautifulSoup(package_page.read())

	package_record = {}

	package_record["name"] = packageName		
	for data in package_data.findAll("p"):
		package_record["description"] = data.get_text()

	previous = ""
	for data in package_data.findAll("table"):
		for comp in data.findAll("td"):
			if previous == "Version:":
				package_record["version"] = comp.get_text()
			
			if previous == "Depends:":
				package_record["depends"] = comp.get_text()
			
			if previous == "Published:":
				package_record["published"] = comp.get_text()

			if previous == "Author:":
				package_record["author"] = comp.get_text()

			if previous == "Maintainer:":
				package_record["maintainer"] = comp.get_text()

			if previous == "License:":
				package_record["license"] = comp.get_text()

			previous = comp.get_text()

	return package_record


with open("packageList.csv") as f:
		for line in f:
			name = line.split('||')[0]
			json_obj = get_name_company(name)
			print json_obj
			collection.insert(json_obj)
