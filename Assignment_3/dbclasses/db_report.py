__author__ = 'KevinMortonMacPro'

import db_access
import db_utility

areas = db_access.get_all_areas()

template = "{:>5}   {:20} {:>15}   {:20}  {:>15}  "
row = template.format("ID", "Area Name", "# of locations", "Avg Value", "Category")
print(row)


for area in areas:
    
    area_id = area['area_id']
    area_location = db_access.get_locations_for_area(area_id)
    area_category = db_access.get_categories_for_area(area_id)
    theCategory = '___'
    
#    print()
    
    for c in area_category:
#        theCategory = float(c['category_id'])
        theCategory = get_category_name_for_area(int(c['category_id']))['name']
#        print(db_access.get_category_name_for_area(int(c['category_id'])))
    
    row = template.format(area_id, area['name'], len(areas), db_utility.get_average_measurements_for_area(area_id),theCategory,
                          )
                        
    
    print(row)
