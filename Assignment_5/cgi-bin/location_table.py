#!/usr/bin/python

__author__ = 'KevinMortonMacPro'

import db_access
import db_utility
import KJM_HTML_Utility
import cgi
import cgitb
cgitb.enable()

areas = db_access.get_all_areas()

def printErrorMSG(formV):
	theMsg =""
	
	if isinstance(formV, list):
		errorMSG  = ''' 
		You may only select a single value.
		<br><p>Form data received:\t{}</p>'''.format(formV)
		
	elif formV.isdigit():
		errorMSG  = ''' 
		The location ID doesn't match any locations in the database.
		<br><p>Form data received:\t{}</p>'''.format(formV)
	
	elif formV == 'None':
		errorMSG = ''' 
			No data was received. 
			<br><p>Form data received:\t{}
			</p>'''.format(formV)
		
	elif str(formV).isalpha() or str(formV).isalnum():
		errorMSG = ''' 
		Only numerical values can be used to query data. 
		<br>Form data received:\t{}<p>
		</p>'''.format(formV)
	
	else:
		errorMSG = '''
		The location ID doesn't match any locations in the database.
		<br><p>Form data received:\t{}
		</p>'''.format(formV)

	print(KJM_HTML_Utility.htmlHeader("Error"))

	print('''
		<body> <form method="post" action="/cgi-bin/area_selection.py"><h2>''')
	print(errorMSG)
		
	print('''
		</h2></select>
			''')
	print('''
		<div style="text-align: center;">
		<input type="submit" value="formAreaID"/>
		</body>
		</html>
		''')	

# ------------------------------------| Table Creation|----------------------------------------------
def getTableHeaderRow():
    tableHeaderRowString = (u"""
	<table class="grid">
    <thead>
	<tr>
		<th>Select</th>
		<th>ID</th>
		<th>Name</th>
		<th>Altitude</th>
	  </tr>
      </thead>
       <tbody>
				""");
    return tableHeaderRowString

# ------------------------------------| CGI|----------------------------------------------
form = cgi.FieldStorage()
	
try:
	formAreaID = form.getvalue('area_id')

	if formAreaID is None:
		printErrorMSG('NoneType')
		
	elif isinstance(formAreaID, list):
		printErrorMsg(formAreaID)
		
	elif not db_access.get_area_by_id(formAreaID):
		printErrorMSG(formAreaID)
		
# ------------------------------------| HTML Page start |------------------------------------
	else:
		selectedArea = db_access.get_area_by_id(formAreaID)
				
		print(KJM_HTML_Utility.htmlHeader("Selected Area"))
		print('''
		<body>
		''')

		theAreaName = str()
		theAreaID = 0

		for i in selectedArea:
			theAreaName = i['name']
			theAreaID = i['area_id']
			print("<h1>Location information for " + theAreaName +"</h1>")
			
		area_locations = db_access.get_locations_for_area(theAreaID)
		if area_locations:
			# create a table for the location
			print('''
			<table class="grid">
			    <thead>
				<tr>
					<th>Select</th>
					<th>ID</th>
					<th>Name</th>
					<th>Altitude</th>
				  </tr>
			      </thead>
			       <tbody>

				<html>
				<head>
					<meta charset="UTF-8">
					<title>Select an Location</title>
				</head>
				<body>
					<form method="get" action="/cgi-bin/measurement_table.py">
					<h2>Select an Location</h2>
					
			''')

			for aLocation in area_locations:
				
				theLocationID = str(aLocation['location_id'])
				radioButtonArea = "<input type=\"radio\" name=\"location_id\" value=\" " + str(theLocationID) + "\" ></td>" 
				rowList = [str(radioButtonArea), theLocationID, aLocation['name'], aLocation['altitude']]
				
				for i in KJM_HTML_Utility.createTableFromList(rowList):
					print(i)
					
			print("</tbody>")
			print("</table>")
			print('''
			</select>
			<div style="text-align: center;">
			<input type="submit" value="Create Measurement Table"/>
			''')

		else:
			print('''
			No associated locations found
			''')
			
		print('''
			    </div>
			</form>
			</body>
			</html>
		''')

except Exception as exc:
	
	printErrorMSG(formAreaID)	
