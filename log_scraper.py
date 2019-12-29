# Project: Traffic Analysis
# Author: Jacob Grubb
# Date: December 2019
# File: log_scraper.py
# Description: Python script for parsing statistics from ssh logs

#Import list
import re
import sys

def getUsers(fileName):
	if(len(sys.argv) != 2):
		print("Syntax Error,", "Correct Syntax:\npython3", sys.argv[0], "<Log file to analyze>")
		sys.exit(1)
	fileLines = []
	try:
		with open(sys.argv[1], 'r') as inFile:
			fileLines = inFile.readlines()
	except IOError as error:
		print("IO error: {0}".format(error))
		sys.exit(2)
	users = []
	#parse the file
	return users


def getAddress(fileName):
	if(len(sys.argv) != 2):
		print("Syntax Error,", "Correct Syntax:\npython3", sys.argv[0], "<Log file to analyze>")
		sys.exit(1)
	fileLines = []
	try:
		with open(sys.argv[1], 'r') as inFile:
			fileLines = inFile.readlines()
	except IOError as error:
		print("IO error: {0}".format(error))
		sys.exit(2)
	addresses = []
	#parse the file
	return addresses

if __name__ == "__main__":
	with open("common_user.txt", "w") as outFile:
		outFile.writelines(getUsers(fileName))
	with open("common_ip.txt", "w") as outFile:
		outFile.writelines(getAddress(fileName))
