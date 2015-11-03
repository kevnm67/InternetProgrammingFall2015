#! /usr/bin/python3

__author__ = 'KevinMortonMacPro'

import webbrowser


# ------------------------------------| HTML FILE CREATION |---------------------------------------------- #
def cgiHeader():
	print("Content-Type: text/html")
	
def htmlHeader(headerTitle):
	#Creates the top of the HTML file with an "about" section for notes
	readMeText = "<!-- \n\tKevin Morton\n\tInternet Programming\n\tAssignment 5\n-->\n\n"
	
	htmlStartTag = '''<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
		<link rel="stylesheet" type="text/css" href="Style1.css">
	'''
	
	theTitle = "<title>" + headerTitle + "</title>\n</head>\n\n"
	
	return readMeText + htmlStartTag + theTitle

# ------------------------------------| TAG CREATION |---------------------------------------------- #
def countSymbol(symbol,theString):
	# Count the number of occurrences the delimiter is found in the string
	theCount = 0
		
	for i in theString:
		if i == symbol:
			theCount+=1
		
	return theCount

# ------------------------------------| Open in browser |---------------------------------------------- #
def browserOpenPage(webpagePath):
	#File path of HTML file to open in webbrowser
		
	webpagePath = 'file:///Users/KevinMortonMacPro/Documents/KSU_Programming_Projects/InternetProgrammingAssignments/Assignment_5/' + 'helloworld.html'
		
	webbrowser.open_new_tab(webpagePath)

