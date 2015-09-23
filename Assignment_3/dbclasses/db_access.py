__author__ = 'KevinMortonMacPro'

import sqlite3
from os.path import split, join

conn = sqlite3.connect("measures.sqlite")

def get_connection():
     this_dir = split(__file__)[0]

     fname = join(this_dir, "measures.sqlite")
     conn = sqlite3.connect(fname)
     conn.row_factory = dictionary_factory
     return conn

def dictionary_factory(cursor, row):
    """
    Create a dictionary from rows in a cursor result.
    The keys will be the column names.
    :param cursor: A cursor from which a query row has just been fetched
    :param row: The query row that was fetched
    :return: A dictionary associating column names to values
    """
    col_names = [d[0] for d in cursor.description]
    return dict(zip(col_names, row))
    
def do_command(cmd, args=[]):
    try:
        conn = get_connection()
        crs = conn.cursor()
        crs.execute(cmd, args)
        return crs.fetchall()
    finally:
        conn.close()
        
# ------------------------------------| Methods |----------------------------------------------
def get_all_areas():
    """
    Returns a list of dictionaries representing all the rows in the
    area table.
    """
    return do_command('SELECT * FROM area')

#################################################### 
def get_locations_for_area(area_id):
    """
    Return a list of dictionaries giving the locations for the given area.
    """
    return do_command('SELECT * FROM location WHERE location_area is?',[area_id])

#################################################### 
def get_measurements_for_location(location_id):
    """
    Return a list of dictionaries giving the measurement rows for the given location.
    """
    return do_command('SELECT * FROM measurement WHERE measurement_location is ?',[location_id])

#################################################### 
def get_categories_for_area(area_id):
    """
    Return a list of rows from the category table that all contain the given area.
    """
    results = do_command('SELECT * FROM category_area WHERE area_id is?',[area_id])
    if not results:
        return None
    else:
        return do_command('SELECT * FROM category WHERE category_id is?',[results[0]['category_id']])

print(get_categories_for_area(3))