#!/usr/bin/python

__author__ = 'KevinMortonMacPro'

import KJM_HTML_Utility
import cgi
import cgitb
cgitb.enable()

print("Content-Type: text/html; charset=UTF-8")
print("")

print ('''

<!DOCTYPE html>
<html>
	<head>
		<title>{}</title>
		<link rel="stylesheet" type="text/css" href="/style1.css"/>
	</head>
	<body>
'''.format("Press the button to test the script"))

print('''
	<html>
	<head>
		<meta charset="UTF-8">
		<title>Select an Area</title>
	</head>
	<body>
	
	<h2>Location Table test 1</h2>
	<hr>
	<a href="/cgi-bin/location_table.py?area_id=2&area_id=5">Multiple selected</a>
	
	<form action="/cgi-bin/location_table.py" method="get">
	
	TEST 2: <input type="text" name="area_id" value="11x33">  
	<input type="submit" value="Submit" />
	</form>
	
	<form action="/cgi-bin/location_table.py" method="get">
	TEST 3: <input type="text" name="area_id" value="1111">  
	<input type="submit" value="Submit" />

	</form>
	<hr>

	<h2>Measurement Table test 1</h2>
	<form action="/cgi-bin/measurement_table.py" method="get">
	
	TEST 1: <input type="text" name="location_id" value="22222">  
	<input type="submit" value="Submit" />
	</form>
	
	<form action="/cgi-bin/measurement_table.py" method="get">
		
		TEST 2: <input type="text" name="location_id" value="2xc3">
		<input type="submit" value="Submit" />
		</form>
	
	<form action="/cgi-bin/measurement_table.py" method="get">
	TEST 3: <input type="text" name="location_id" value=""> 
	<input type="submit" value="Submit" />
	
	</form>
	</body>
	</html>
	
''')