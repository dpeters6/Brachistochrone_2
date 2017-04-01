# filename:      map.py
# author:        Henry Mitchell
# creation date: 01 Apr 2017

# description:   Make pretty maps

import mapbox as mb

static = mb.Static()
ds = mb.Datasets()
dsid = 'cj0zcvgfj03eq32sd22ojxt9f'
buildings = []
names = []

building_ids = {
    'bllngs' : '09f7bdfbd310df3f188acb4e50ce7d14',
    # 'cook' : '5a889d124be37b8fcb5f6bc37742b644',
    # 'dana' : '50275fb6e7bf8ab75427af9e8e00a380',
    # 'davis' : '16e615d9bc43cf35f627d2411079d3fd',
    # 'discovery' : '199877b08cc3de4a4ad88ba65f730371',
    'flemin' : '2e3556350cf72ea054bd354e46899318',
    'hsrf' : '6f5e9eb85ae1129a1408d927cc2119d4',
    'morril' : '310ee53ca0599174af92743ec579e94d',
    'omanex' : '21f2116702d35d8e21e706fb3dd6a311',
    'oldmil' : '20ab696c02c2341b735d6883209dead3',
    'perkin' : '586f12524384b40ad4551ad7087a62d4',
    'rt thr' : '56eb9a5c25971d8eba6269e35627238e',
    # 'stafford greenhouse' : '321c949c44b660700cc7e38117574b5a',
    'staffo' : '10c79f8764a71e16fac9ee2ed3945c94',
    'terril' : '3b5247428424128c026c94c7922e9748',
    'torrey' : '49699344e48e31625af65afed19bafdf',
    'waterm' : '6edc7477a6e49a24a3aef204f22a766a',
    'willms' : '0c756ccb40fa20f0164244efc74f26b0',
    }

def make_map(features = None):
    response = static.image('mapbox.pencil', lon=-73.196091, lat=44.476947, z=16, features = features)
    with open('static/images/map.png', 'wb') as output:
        _ = output.write(response.content)

def add_building(building):
    '''Add a building to the map'''
    if not building in buildings:
        return()
    building_id = building_ids[building.lower()]
    feature = ds.read_feature(dsid, building_id)
    buildings.append(feature.json())
    make_map(buildings)
    name = building_name(building)
    if not name in names:
        names.append(building_name(building))

def clear_map():
    global buildings, names
    buildings = []
    names = []
    make_map()

def building_name(building):
    building_id = building_ids[building.lower()]
    feature = ds.read_feature(dsid, building_id)
    return(feature.json()['properties']['Building'])

def list_names():
    return(names)
