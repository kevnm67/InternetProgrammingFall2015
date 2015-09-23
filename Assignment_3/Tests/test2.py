__author__ = 'Ben Setzer'

import unittest
import db_utility


def filter_first(list, predicate):
    for x in list:
        if predicate(x):
            return x
    return None

class TestDbFunctions(unittest.TestCase):
    def testNumberAreas(self):
        areas = DBaccess.get_all_areas()
        self.assertEqual(7, len(areas))

    def testOneArea(self):
        areas = DBaccess.get_all_areas()
        k = filter_first(areas, lambda r: r['area_id'] == 3)
        self.assertEqual('Kennesaw', k['name'])

    def testNumberOfLocations(self):
        locs = DBaccess.get_locations_for_area(3)
        self.assertEqual(len(locs), 4)

    def testOneLocation(self):
        locs = DBaccess.get_locations_for_area(3)
        m = filter_first(locs, lambda r: r['location_id'] == 18)
        self.assertEqual('Mall', m['name'])

    def testNumberOfMeasurements(self):
        meas = DBaccess.get_measurements_for_location(18)
        self.assertEqual(10, len(meas))

    def testOneMeasurement(self):
        meas = DBaccess.get_measurements_for_location(18)
        m = filter_first(meas, lambda r: r['measurement_id'] == 1803)
        self.assertAlmostEqual(61.11457551359794, m['value'], delta=1e-10)

    def testNumberOfCategories(self):
        cats = DBaccess.get_categories_for_area(3)
        self.assertEqual(1, len(cats))

    def testOneCategory(self):
        cats = DBaccess.get_categories_for_area(3)
        m = filter_first(cats, lambda r: r['category_id'] == 32)
        self.assertEqual('East', m['name'])

    def testAverageMeasurement(self):
        avg = db_utility.get_average_measurements_for_area(3)
        self.assertAlmostEqual(61.77813528637446,avg, delta=1e-10)

    def testAverageMeasurementMissing(self):
        avg = db_utility.get_average_measurements_for_area(7)
        self.assertEqual(None, avg)

    def testNumberOfLocations2(self):
        numLoc = db_utility.number_of_locations_by_area(3)
        self.assertEqual(4, numLoc)

# if __name__ == "__main__":
#     unittest.main()