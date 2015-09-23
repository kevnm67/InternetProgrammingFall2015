__author__ = 'KevinMortonMacPro'

import db_access
import db_utility

areas = db_access.get_all_areas()
template = "{:>5}   {:20} {:<20} {:.5}  {:<20}  "

row = template.format("ID", "Area Name", "# of locations", "Avg Value", "Category")
print(row)

for area in areas:    
    area_id = area['area_id']
    area_location = db_access.get_locations_for_area(area_id)
    area_category = db_access.get_categories_for_area(area_id)
    theCategory = ''
   
    if not area_category:
        theCategory = 'none'
    else:
        theCategory = area_category[0]['name']
  
    avgMeasurementString = str( db_utility.get_average_measurements_for_area(area_id))
    if not db_utility.get_average_measurements_for_area(area_id):
        avgMeasurementString = '----------'
        
  
    row = template.format(area_id, area['name'], len(areas), avgMeasurementString,theCategory)
    print(row)
    
    	
