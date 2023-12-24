# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import defaultdict
import pprint

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

shakeCounters = defaultdict(int)

for dataitem in data["features"]:
    shakeType = dataitem["properties"]["type"]
    if shakeType is None:
        shakeCounters["other event"] += 1
    else:
        shakeCounters[shakeType] += 1

pprint.pp(shakeCounters)
