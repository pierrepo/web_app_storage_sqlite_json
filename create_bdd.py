# -*- coding: utf-8 -*-
import random
import sqlite3
import json

# https://github.com/joke2k/faker
from faker import Factory
fake = Factory.create('fr_FR')

# Create sqlite connection
conn = sqlite3.connect('places_db.sqlite')
curs = conn.cursor()
curs.execute('DROP TABLE IF EXISTS places')
conn.commit()
curs.execute('CREATE TABLE places(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, address TEXT, city TEXT, lat REAL, lon REAL, tel1 TEXT, tel2 TEXT)')

# Create json db
db = []

for i in range(2000):
    name = "Pharmacie " + fake.last_name()

    address = fake.street_name() + "\n"
    address_comp1 = "face entreprise " + fake.last_name()
    address_comp2 = "arrêt de bus " + fake.last_name()
    address += random.choice([address_comp1, address_comp2])

    place = random.choice(['PNR', 'BZV'])

    city = ""
    lat = 0.0
    lon = 0.0
    if place == 'PNR':
        coords = (-4.787914, 11.864805)
        city = "Pointe-Noire"
        lat = fake.geo_coordinate(center=coords[0], radius=0.001)
        lon = fake.geo_coordinate(center=coords[1], radius=0.001)
    if place == 'BZV':
        coords = (-4.261874, 15.252113)
        city = "Brazzaville"
        lat = fake.geo_coordinate(center=coords[0], radius=0.001)
        lon = fake.geo_coordinate(center=coords[1], radius=0.001)

    tel1 = random.choice(['05', '06']) + "".join([ str(random.randint(0, 9)) for n in range(7)])
    tel2 = random.choice(['05', '06']) + "".join([ str(random.randint(0, 9)) for n in range(7)]) 

    # output data
    print(i)
    print(name)
    print(address)
    print(city)
    print(lat, lon)
    print(tel1)
    print(tel2)
    # store data in sqlite
    try: 
        curs.execute('INSERT INTO places(name, address, city, lat, lon, tel1, tel2) VALUES(?,?,?,?,?,?,?)', (name, address, city, float(lat), float(lon), tel1, tel2))
    except:
        print(name)
        print(address)
        print(city)
        print(lat, lon)
        print(tel1)
        print(tel2)
    # store in json
    db.append( {"id":i, "name":name, "address":address, "city":city, "lat":float(lat), "lon":float(lon), "tel1":tel1, "tel2":tel2} )

# save and close SQLite database
conn.commit()
curs.close()
conn.close()

# save json database
with open("places_db.json", "w") as json_file:
    json_file.write("places = ")
    json.dump(db, json_file, sort_keys = True, indent=4)

