import matplotlib.pyplot as plt
import numpy as na
import db_access,db_utility

# ------------------------------------| Graph results |----------------------------------------------
def graphIt():
    areas = db_access.get_all_areas()
    placesList = []
    theAvgMeasurements = []

    for a in areas:
        placesList.append(a['name'])
        theAvg = db_utility.get_average_measurements_for_area(a['area_id'])
        if not theAvg:
            theAvg = 0
        theAvgMeasurements.append(theAvg)

    print(theAvgMeasurements)
    values = tuple(theAvgMeasurements)
    ind = na.array(range(len(values))) + 0.5
    width = 0.35
    plt.bar(ind, values, width, color='r')
    plt.ylabel('Average Measurement')
    plt.title('Areas')

    plt.xticks(ind + width / 2, tuple(placesList))
    plt.show()


graphIt()
