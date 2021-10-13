import os
import sys
import json

template = {"type": "FeatureCollection", "features": []}

files = os.listdir("./uk-postcode-polygons/geojson")

for file in files:

    filepath = os.path.join("./uk-postcode-polygons/geojson", file)

    with open(filepath) as json_file:
        data = json.load(json_file)

    template["features"].extend(data["features"])

with open('Full.geojson', 'w') as outfile:
    json.dump(template, outfile)
