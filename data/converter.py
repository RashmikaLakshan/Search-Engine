import csv
import json
import os

currentDirectory = os.path.dirname(os.path.abspath(__file__))


# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
	
	# create a dictionary
	data = []
	
	# Open a csv reader called DictReader
	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)
		
		for rows in csvReader:
			data.append(rows) 

	# Open a json writer, and use the json.dumps()
	# function to dump data
	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(data, indent=4))
		

# Decide the two file paths according to your
# computer system
cseFilePath = currentDirectory + '../data/book_writers.xlsx'
jsonFilePath = currentDirectory + '../data/authors.json'

# Call the make_json function
make_json(cseFilePath, jsonFilePath)
