# filename:      map.py
# author:        Henry Mitchell
# creation date: 01 Apr 2017

# description:   Make pretty maps

import mapbox as mb

service = mb.Static()
ds = mb.Datasets()
dsid = 'cj0zcvgfj03eq32sd22ojxt9f'
buildings = []

building_ids = {
    'billings' : '09f7bdfbd310df3f188acb4e50ce7d14',
    'williams' : '0c756ccb40fa20f0164244efc74f26b0',
    'stafford' : '10c79f8764a71e16fac9ee2ed3945c94',
    'davis' : '16e615d9bc43cf35f627d2411079d3fd',
    'discovery' : '199877b08cc3de4a4ad88ba65f730371',
    'old mill' : '20ab696c02c2341b735d6883209dead3',
    'old mill annex' : '21f2116702d35d8e21e706fb3dd6a311',
    'fleming' : '2e3556350cf72ea054bd354e46899318',
    'morrill' : '310ee53ca0599174af92743ec579e94d',
    'stafford greenhouse' : '321c949c44b660700cc7e38117574b5a',
    'terrill' : '3b5247428424128c026c94c7922e9748',
    'torrey' : '49699344e48e31625af65afed19bafdf',
    'dana' : '50275fb6e7bf8ab75427af9e8e00a380',
    'royal tyler theater' : '56eb9a5c25971d8eba6269e35627238e',
    'perkins' : '586f12524384b40ad4551ad7087a62d4',
    'cook' : '5a889d124be37b8fcb5f6bc37742b644',
    'waterman' : '6edc7477a6e49a24a3aef204f22a766a',
    'health science research facility' : '6f5e9eb85ae1129a1408d927cc2119d4'
    }

def make_map(features = None):
    response = service.image('mapbox.pencil', lon=-73.196091, lat=44.476947, z=16, features = features)
    with open('static/images/map.png', 'wb') as output:
        _ = output.write(response.content)

def add_building(building):
    building_id = building_ids[building.lower()]
    feature = ds.read_feature(dsid, building_id)
    buildings.append(feature.json())
    make_map(buildings)

