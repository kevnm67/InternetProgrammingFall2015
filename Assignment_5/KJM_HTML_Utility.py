#!/usr/bin/python
__author__ = 'KevinMortonMacPro'

import webbrowser

# ------------------------------------| HTML FILE CREATION |---------------------------------------------- #
def writeHTMLFile(aList):
	f = open('helloworld.html','w')
	
	for i in aList:
		f.write(i)
		
	f.close()

def writeHTMLHeader(headerTitle):
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


def replaceSymbolWithTag(aString,symbol,tag):
	#Replace % with proper HTML tags. Even % will be replaced with <html> and odd with </html>
	
	stringCount = countSymbol(symbol,aString)
	closingTag = str(tag).replace("<", "</")
	
	for i in aString:
		
		if i == symbol:
			
			if stringCount % 2 == 0:
				
				#replace even occurences with opening tag
				aString = aString.replace(symbol,tag,1)
			
			else:
				
				#replace odd occurences with closing tag
				aString = aString.replace(symbol,closingTag,1)
		
			stringCount-=1
	
	return aString

def createTableFromStringWithSymbol(aString,symbol):
	return replaceSymbolWithTag(aString, symbol, "")

# ------------------------------------| Open in browser |---------------------------------------------- #
def browserOpenPage(webpagePath):
	#File path of HTML file to open in webbrowser
	
	webpagePath = 'file:///Users/KevinMortonMacPro/Documents/KSU_Programming_Projects/InternetProgrammingAssignments/Assignment_5/' + 'helloworld.html'
	
	webbrowser.open_new_tab(webpagePath)


# ------------------------------------| TEST |---------------------------------------------- #

def testHTMLcreation():
	
	myList = [writeHTMLHeader("Kevins Website"),"<body>\n\n",replaceSymbolWithTag("$kevin$ $goes$ $to$ $store$", "$", "<br>"),"\n\n</body>\n"]
	
	writeHTMLFile(myList)
	
	browserOpenPage("")
	
	
testHTMLcreation()