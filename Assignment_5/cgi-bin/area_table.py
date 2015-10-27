#!/usr/bin/python3

__author__ = 'KevinMortonMacPro'

import db_access
import db_utility
import KJM_HTML_Utility
#import cgi
#import cgitb
#cgitb.enable()

areas = db_access.get_all_areas()

# Generate a report similar to that produced in Assignment #3. 
# Main difference = the table is presented using an HTML table so column widths will not be a problem.
# However, make sure to limit the number of decimal places displayed in the average measurement.

# ------------------------------------| Formatting functions |------------------------------------
def getCategoryString(aList):
    # Pass a list of categories to get a formatted comma separated string
    categoryString = ''
    theCategory = []

    try:
        for i in aList:
            theCategory.append(i['name'])
        countString = len(area_category)

        for i in theCategory:
            categoryString += i
            if countString > 1:
                categoryString += ', '
                countString += -1
    except TypeError:
        categoryString = ''
    return categoryString

# ------------------------------------| Assignment 5 |----------------------------------------------
def getTableHeaderRow():
    # <table class="grid">
    tableHeaderRowString = (u"""
	<table class="grid">
    <thead>
	<tr>
		<th>ID</th>
		<th>Area Name</th>
		<th># of Locations</th>
		<th>Avg Value</th>
		<th>Category</th>
	  </tr>
      </thead>
        
       <tbody>
				""");
    return tableHeaderRowString

print(getTableHeaderRow())

# ------------------------------------| Pretty Print |----------------------------------------------
for area in areas:
    
    area_id = area['area_id']
    area_location = db_access.get_locations_for_area(area_id)
    area_category = db_access.get_categories_for_area(area_id)
    avgMeasurementString = str(db_utility.get_average_measurements_for_area(area_id))

    if not db_utility.get_average_measurements_for_area(area_id):
        avgMeasurementString = '--------'

    rowList = [area_id, area['name'], len(area_location), avgMeasurementString[1:5], getCategoryString(area_category)]

    for i in KJM_HTML_Utility.createTableFromList(rowList):
        print(i)
    
print("</tbody>")
print("</table>")