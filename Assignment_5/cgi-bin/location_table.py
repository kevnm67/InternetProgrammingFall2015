#!/usr/bin/python3

__author__ = 'KevinMortonMacPro'

import cgi
import cgitb
cgitb.enable()
import math

"""
generate a table of locations that belong to an area.
The area will be identified by the area id, passed to the script with the name area_id. 
A header on the page should identify the area by name that was chosen.
The locations will be listed in a table with the location id, the location name and the location altitude.

Each row will also have a radio button, in the first column. 
In the initial page, the first button should be checked. 
There will be a submit button that will cause Script measurement_table.py to be executed sending the id of the selected location to the script using the name location_id.

If there are no locations for the area, then the displayed page should display a suitable message rather than a table.
"""

form = cgi.FieldStorage()

try:
	start = fldstor.getfirst("area_id", 1)
	area_id = form.getfirst("area_id", "").upper() 

except Exception as exc:
	page("One of the values you entered did not convert properly", exc)
	quit()
			
