# Comparison of data storage and query with SQLite and json for a web app

## Data generation

2000 fake (pharmacy) addresses were generated with the `faker` Python module. These addresses were stored in a SQLite database and in a json file.

```bash
python create_db.py
```

Data sample:

```
places = [
    {
        "address": "rue Paris\nface entreprise Goncalves",
        "city": "Pointe-Noire",
        "id": 0,
        "lat": -4.788426,
        "lon": 11.864629,
        "name": "Pharmacie Collin",
        "tel1": "064751455",
        "tel2": "069443823"
    },
    {
        "address": "rue de Bousquet\nface entreprise De Sousa",
        "city": "Brazzaville",
        "id": 1,
        "lat": -4.261567,
        "lon": 15.252074,
        "name": "Pharmacie Auger",
        "tel1": "063708460",
        "tel2": "063012653"
    },
```

File size (for the exact same data):

    - places_db.sqlite: 252 ko
    - places_db.json: 536 ko


## Data query

Data queries were tested with json.js (for SQLite database -- see test_sqlite.html) or with JsonQuery (for json database -- see test_json.html).

Running tests are available here: 

    - (json.js / SQLite)[http://pierrepo.github.io/web_app_storage_sqlite_json/test_sqlite.html] 
    - (JsonQuery / json)[http://pierrepo.github.io/web_app_storage_sqlite_json/test_json.html]

 
