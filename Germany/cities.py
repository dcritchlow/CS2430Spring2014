#!/usr/bin/python

import sqlite3
# conn = sqlite3.connect('germany.db')
conn = sqlite3.connect(':memory:')
conn.text_factory = sqlite3.OptimizedUnicode
c = conn.cursor()

# Create Table for cities
c.execute("CREATE TABLE cities (id INTEGER PRIMARY KEY,name TEXT, description TEXT, starting INTEGER);")

cities = [
    ('Rostock', '', '0'),
    ('Lubeck', 'Home of the best marzipan', '0'),
    ('Hamburg', 'Oma/Opa want to drive under the river - a taxi can do this as well', '0'),
    ('Bremen','', '0'),
    ('Hannover','Consumer Electronics haven - purchase a new iPad at 180 Euros each', '0'),
    ('Kassel','', '0'),
    ('Dusseldorf','', '0'),
    ('Koln','Taxi will be needed to visit the castle 10km away from the hauptbahnhof', '0'),
    ('St. Augustine','', '0'),
    ('Bonn','', '0'),
    ('Wiesbaden','', '0'),
    ('Frankfurt','', '1'),
    ('Mannheim','', '0'),
    ('Karlsruhe','', '0'),
    ('Baden Baden','Oma wants to visit a spa here, therefore, you will need to spend the day', '0'),
    ('Stuttgart','', '1'),
    ('Munchen (Munich)','', '1'),
    ('Nurnberg','', '0'),
    ('Dresden','', '0'),
    ('Leipzig','', '0'),
    ('Berlin','', '1'),
    ('Basel, Switzerland','Opa and Dad want to purchase a nice watch and this is the best place for such a purchase - you will be spending $6k/watch', '0')
]
#Insert data
c.executemany("INSERT INTO cities(name, description, starting) VALUES (?,?,?);", cities)
conn.commit()

# # Print the cities
# c.execute("SELECT name FROM cities WHERE starting=1")
# for row in c:
#     print row

# Create Table for airfare
c.execute("CREATE TABLE airfare (city TEXT, airport TEXT, destination TEXT, time INTEGER, cost INTEGER, calculated INTEGER);")

airfare = [
    ('Chicago', 'ORD', 'BNA', 90, 156.21, 4.21),
    ('Nashville', 'BNA', 'ORD', 100, 156.21, 4.21),
    ('Nashville', 'BNA', 'FRA', 1049, 617.76, 11.90),
]

# Insert data
c.executemany("INSERT INTO airfare(city, airport, destination, time, cost, calculated) VALUES (?,?,?,?,?,?);", airfare)
conn.commit()

# Create Table for airport distances
c.execute("CREATE TABLE airport_distance (airport TEXT, destination TEXT, kilometers INTEGER, miles INTEGER);")

airport_distance = [
    ('ORD', 'BNA', 658, 409),
    ('BNA', 'FRA', 7350, 4570),
]

# Insert data
c.executemany("INSERT INTO airport_distance(airport, destination, kilometers, miles) VALUES (?,?,?,?);", airport_distance)
conn.commit()

# Print airport_distance
c.execute("SELECT kilometers FROM airport_distance WHERE airport='ORD' and destination='BNA' OR airport='BNA' and destination='ORD'")
for row in c:
    print row
conn.close()
