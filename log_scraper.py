# Project: Traffic Analysis
# Author: Jacob Grubb
# Date: December 2019
# File: log_scraper.py
# Description: Python script for parsing statistics from ssh logs

#Import list
import re
import sys
from collections import Counter

def getUsers(fileName):
	fileLines = []
	try:
		with open(fileName, 'r') as inFile:
			fileLines = inFile.readlines()
	except IOError as error:
		print("IO error: {0}".format(error))
		sys.exit(2)
	users = []
	lineRE = re.compile("invalid user (\w+) from (\d{2,3}.\d{2,3}.\d{2,3}.\d{2,3})")
	#parse the file
	for line in fileLines:
		match = lineRE.search(line)
		if(match):
			users.append(match.group(1))
	userCount = Counter(users).most_common()
	#Returns a list of tuples of the form:
	# (username, # of occurences)
	return userCount


def getAddress(fileName):
	fileLines = []
	try:
		with open(fileName, 'r') as inFile:
			fileLines = inFile.readlines()
	except IOError as error:
		print("IO error: {0}".format(error))
		sys.exit(2)
	addresses = []
	lineRE = re.compile("invalid user (\w+) from (\d{2,3}.\d{2,3}.\d{2,3}.\d{2,3})")
	#parse the file
	for line in fileLines:
		match = lineRE.search(line)
		if(match):
			addresses.append(match.group(2))
	addressCount = Counter(addresses).most_common()
	#Returns a list of tuples of the form:
	# (address, # of occurences)
	return addressCount

def getBoth(fileName):
	fileLines = []
	try:
		with open(fileName, 'r') as inFile:
			fileLines = inFile.readlines()
	except IOError as error:
		print("IO error: {0}".format(error))
		sys.exit(2)
	addresses = []
	lineRE = re.compile("invalid user (\w+) from (\d{2,3}.\d{2,3}.\d{2,3}.\d{2,3})")
	addresses = []
	users = []
	#parse the file
	for line in fileLines:
		match = lineRE.search(line)
		if(match):
			users.append(match.group(1))
			addresses.append(match.group(2))
	userCount = Counter(users).most_common()
	addressCount = Counter(addresses).most_common()
	return userCount, addressCount

if __name__ == "__main__":
	if(len(sys.argv) != 2):
		print("Syntax Error,", "Correct Syntax:\npython3", sys.argv[0], "<Log file to analyze>")
		sys.exit(1)
	userCount, addressCount = getBoth(sys.argv[1])
	with open("common_user.txt", "w") as outFile:
		for item in userCount:
			outFile.write(item[0] + ": " + str(item[1]) + '\n')
	with open("common_ip.txt", "w") as outFile:
		for item in addressCount:
			outFile.write(item[0] + ": " + str(item[1]) + '\n')
