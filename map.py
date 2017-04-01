# filename:      map.py
# author:        Henry Mitchell
# creation date: 01 Apr 2017

# description:   Make pretty maps

import mapbox as mb

service = mb.Static()

def make_map(features = None):
    response = service.image('mapbox.pencil', lon=-73.196091, lat=44.476947, z=17, features = features)
    with open('static/images/map.png', 'wb') as output:
        _ = output.write(response.content)

make_map()
