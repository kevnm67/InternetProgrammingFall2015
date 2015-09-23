__author__ = 'KevinMortonMacPro'

import db_access

def get_average_measurements_for_area(area_id):
    """
    Returns the average value of all measurements for all locations in the given area.
    Returns None if there are no measurements.
    """
    crs_two = db_access.get_locations_for_area(area_id)    
    averageValue = 0.0
    total = 0.0
    item = 0.0
    
    for row in crs_two:
        anID = int(row['location_id'])
        measurementCRS = db_access.get_measurements_for_location(anID)

        for measurementRow in measurementCRS:
            total += float(measurementRow['value'])
            item +=1
    
    if item == 0:
        return None
    else:
        averageValue = total/item
        return averageValue

def number_of_locations_by_area(area_id):
    """
    Returns the number of locations for the given area.
    """
    return len(db_access.get_locations_for_area(area_id))
  

#################### Tempory - delete me ####################   
def printLocationsWithMeasurements(allLocation,allMeasurements):
    for i in allLocation:
        print(i,'\n')
    print('\nlocations\n')
    for i in allMeasurements:
        print(i,'\n')
############################################################


avg = get_average_measurements_for_area(7)
print('avg calc:\t',avg,'\n')
print('-'*10,'\nexpected:\t 61.77813528637446 ')


#print(printLocationsWithMeasurements(allLocation, allMeasurements))
