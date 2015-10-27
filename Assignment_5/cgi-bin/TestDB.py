#!/usr/bin/env python
import sys
import db_access
import db_utility
import KJM_HTML_Utility

areas = db_access.get_all_areas()


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


def printFields():
    """ Connects to the table specified by the user and prints out its fields in HTML format used by Ben's wiki. """
    fields = db_access.get_all_areas()
    counter = 0
    print(u"""
	<table border="0"><tr><th>order</th><th>name</th><th>type</th><th>description</th></tr>
	<tbody>
	""");

    for area in areas:
        counter = counter + 1

        area_id = area['area_id']
        area_location = db_access.get_locations_for_area(area_id)
        area_category = db_access.get_categories_for_area(area_id)
        avgMeasurementString = str(db_utility.get_average_measurements_for_area(area_id))

        if not db_utility.get_average_measurements_for_area(area_id):
            avgMeasurementString = '--------'

        name = area_id, area['name']
        locations = len(area_location)
        avgMeasurement = avgMeasurementString
        theCategory = getCategoryString(area_category)


        #		rowList = [area_id, area['name'], len(area_location), avgMeasurementString, getCategoryString(area_category)]

        print("<tr><td>" + str(counter) + '</td><td>' + name + '</td><td>' + type + '</td><td></td></tr>')
        print("</tbody>")
        print("</table>")


for area in areas:

    area_id = area['area_id']
    area_location = db_access.get_locations_for_area(area_id)
    area_category = db_access.get_categories_for_area(area_id)
    avgMeasurementString = str(db_utility.get_average_measurements_for_area(area_id))

    if not db_utility.get_average_measurements_for_area(area_id):
        avgMeasurementString = '--------'

    rowList = [area_id, area['name'], len(area_location), avgMeasurementString, getCategoryString(area_category)]

    allRows = KJM_HTML_Utility.createTableFromList(rowList)

    for i in allRows:
        KJM_HTML_Utility.writeHTMLFile(str(i))

    print(getCategoryString(area_category))
