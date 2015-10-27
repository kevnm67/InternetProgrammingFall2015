#!/usr/bin/python3

__author__ = 'KevinMortonMacPro'

import db_access
import db_utility
import KJM_HTML_Utility

areas = db_access.get_all_areas()

# Script area_selection.py will generate a form with a list of names of areas using the select tag with a size of 10.
# There will be a submit button that will cause Script -> location_table.py to be executed,
# sending the id of the selected area to the script using the name area_id.

def printDocuementStart():

	areaList = []
	areaIDList = []
	for area in areas:
		areaList.append(area['name'])	
		areaIDList.append("<option value=" + str(area['area_id']) + ">" + area['name'] + "</option>")

	documentStart = """
		<html>
			<head>
				<meta charset="UTF-8">
				<title>Select an Area</title>
			</head>
			<body>
				<form method="get" action="/cgi-bin/location_table.py">
				<h2>Select an Area</h2>
				<select name="area_id" size="10" multiple>
		"""

	listEnding = """
	</select>
		<div style="text-align: center;">
	<input type="submit" value="Submit" />   
	</div>
		</form>
	</body>
	</html>
	"""
	print(KJM_HTML_Utility.htmlHeader("Select an Area"))
	
	print(documentStart)
	for i in areaIDList:
		print("\t" + i)
	print(listEnding)
	
	documentEnding = """
	</body>
	</html>
	"""
	
	#http://localhost:8080/cgi-bin/location_table.py?area_id=
#send the selected id to the script ->  cause Script location_table.py to be executed, sending the id of the selected area to the script using the name area_id.

printDocuementStart()

#http://localhost:8080/cgi-bin/function_table.py?start=1&end=10&numrows=11&function=square&function=log2
