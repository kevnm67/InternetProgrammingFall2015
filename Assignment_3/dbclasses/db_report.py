__author__ = 'KevinMortonMacPro'

import db_access
import db_utility

areas = db_access.get_all_areas()
# ------------------------------------| Formatting |----------------------------------------------
template = "{:>5}   {:20} {:<20} {:.5}  {:<20}  "
row = template.format("ID", "Area Name", "# of locations", "Avg Value", "Category")
print(row)

# ------------------------------------| Pretty Print |----------------------------------------------
for area in areas:  
    area_id = area['area_id']
    area_location = db_access.get_locations_for_area(area_id)
    area_category = db_access.get_categories_for_area(area_id)
    
    theCategory = ''
    theS = ''
    countNum = 0
    
    try:
        print('area count\t',len(area_location))
        for i in area_category:
           theCategory += i['name']
    except TypeError:
        theCategory = 'None'

    avgMeasurementString = str( db_utility.get_average_measurements_for_area(area_id))
    
    if not db_utility.get_average_measurements_for_area(area_id):
        avgMeasurementString = '----------'
        
        
# -------| Final output |----------------------------------------------
    row = template.format(area_id, area['name'], len(area_location), avgMeasurementString,theCategory)
    print(row)
    
    
    