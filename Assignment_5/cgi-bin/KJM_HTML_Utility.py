#!/usr/bin/python

__author__ = 'KevinMortonMacPro'

import webbrowser

# ------------------------------------| HTML FILE CREATION |---------------------------------------------- #
def writeHTMLFile(aList):
	f = open('helloworld.html','w')
	for i in aList:
		f.write(str(i))
	f.close()

# ------------------------------------| HTML FILE CREATION |---------------------------------------------- #
def cgiHeader():
	print("Content-Type: text/html; charset=UTF-8")

def documentTitleForAssignment(assignmentNumber):
	return "\n<!-- \n\tKevin Morton\n\tInternet Programming\n\tAssignment" + str(assignmentNumber) + "\n-->\n\n"

def htmlHeader(headerTitle):
	htmlStartTag = '''
<!DOCTYPE html>
	<html>
		<head>
			<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
			<link rel="stylesheet" type="text/css" href="/style1.css"/>
	'''
	theTitle = "<title>" + headerTitle + "</title>\n</head>\n\n"

	return "Content-Type: text/html; charset=UTF-8\n\n" + documentTitleForAssignment("5 ") + htmlStartTag + theTitle

# ------------------------------------| TAG CREATION |---------------------------------------------- #
def countSymbol(symbol,theString):
	'''Count the number of occurrences the delimiter is found in the string'''
	theCount = 0

	for i in theString:
		if i == symbol:
			theCount+=1
	return theCount

def replaceSymbolWithTag(aString,symbol,tag):
	'''
		Replace % with proper HTML tags. Even % will be replaced with <html> and odd with </html>
	'''
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
					
def createTableFromList(list):
	tableList = []
	tableHeaderRowString = (u"""
	<tr>
					""");
	tableList.append(tableHeaderRowString)
	
	for i in list:
		tableList.append("\t\t<td>" + str(i) + "</td>")
	tableList.append("</tr>")
	
	return tableList

def createTableHeaderFromList(list):
	tableList = []
	
	tableHeaderRowString = (u"""
	<table class="grid">
	    <thead>
		<tr>
					""");
	tableList.append(tableHeaderRowString)
	
	for i in list:
		tableList.append("\t\t<tr>" + str(i) + "</tr>")
	tableList.append("</tr></thead></tbody>")
	
	return tableList
	
def errorWithMSG(msg):
	theEnd = '''
		</body>
		</html>
		'''
	return htmlHeader("Error") + msg + theEnd


# ------------------------------------| Open in browser |---------------------------------------------- #
def browserOpenPage(webpagePath):
	#File path of HTML file to open in webbrowser
	webpagePath = 'file:///Users/KevinMortonMacPro/Documents/KSU_Programming_Projects/InternetProgrammingAssignments/Assignment_5/' + 'helloworld.html'
	webbrowser.open_new_tab(webpagePath)

# ------------------------------------| TEST |---------------------------------------------- #
def testHTMLcreation():
	testHeader = htmlHeader("Kevins Website")
	myList = [testHeader,"<body>\n\n",replaceSymbolWithTag("$kevin$ $goes$ $to$ $store$", "$", "<br>"),"\n\n</body>\n"]
	writeHTMLFile(myList)

	browserOpenPage("")

