#!/usr/bin/python

__author__ = 'KevinMortonMacPro'

import db_access
import db_utility
import KJM_HTML_Utility
import cgi
import cgitb
cgitb.enable()

def printErrorMSG(formV):
	theMsg =""
	
	if formV.isdigit():
		errorMSG  = ''' 
		The location ID doesn't match any locations in the database.
		<br><p>Form data received:\t character found was:\t{}</p>'''.format(formLocationID)
	
	elif formV == 'None':
		errorMSG = ''' 
			No data was received. 
			<br><p>Form data received:\t{}
			</p>'''.format(formLocationID)
		

	elif str(formV).isalpha() or str(formV).isalnum():
		errorMSG = ''' 
		Only numerical values can be used to query data. 
		<br>Form data received:\t character found was:\t{}<p>
		</p>'''.format(formLocationID)
	
	else:
		errorMSG = '''
		The location ID doesn't match any locations in the database.<br><p>Form data received:\t character found was:\t{}
		</p>'''.format(formLocationID)


	print(KJM_HTML_Utility.htmlHeader("Error"))

	print('''
		<body>
		<form method="post" action="/cgi-bin/area_selection_test1.py">
		<h2>''')
	print(errorMSG)
		
	print('''
			</h2>
			</select>
			''')
	
	print('''
		<div style="text-align: center;">
		<input type="submit" value="formAreaID"/>
		</body>
		</html>
		''')	
		
# ------------------------------------| start |----------------------------------------------
form = cgi.FieldStorage()
	
try:
	formLocationID = form.getvalue('location_id')

	if not db_access.get_location_by_id(formLocationID):	
		printErrorMSG(str(formLocationID))

			
# ------------------------------------| good data received |----------------------------------------------	
	else:
		selectedLocation = db_access.get_location_by_id(formLocationID)
		measurementsForSelectedLocation = db_access.get_measurements_for_location(formLocationID)

		# ------------------------------------| HTML Page start |------------------------------------
		print(KJM_HTML_Utility.htmlHeader("Selected Location"))
		print('''
		<body>
		''')
		
		for i in selectedLocation:
			
			#header identify the area and location by name.
			locArea = db_access.get_area_by_id(i['location_area'])
			itsName = str()
			for aName in locArea:
				itsName = aName['name']
			print("<h1>" + str(i['name']) + "</h1>\n<h2> Area: " + str(itsName)  + "</h2>")

		if measurementsForSelectedLocation:
			print(u"""
				<table class="grid">
			    <thead>
				<tr>
					<th>Measurement ID</th>
					<th>ID</th>
					<th>Value</th>
					
				  </tr>
			      </thead>
			  
			       <tbody>
							""");
			measurementValue = 0
			rowList = []
			
			for i in measurementsForSelectedLocation:
				measurementValue += i['value'] 
				rowList = [i['measurement_location'],i['measurement_id'], i['value']]
				for i in KJM_HTML_Utility.createTableFromList(rowList):
					print(i)
									
			avgMeasurementString = str(db_utility.get_average_measurement_for_location(formLocationID))
			
			if not db_utility.get_average_measurement_for_location(formLocationID):
				avgMeasurementString = '--------'
			

			print("</tbody>")
			print("</table>")
			print("<div><h3>Average measurement:\t" + avgMeasurementString + "</h3></div>" )

		else:
			print('none found')
	
		
except Exception as exc:
	printErrorMSG(str(formLocationID))