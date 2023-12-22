# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

def getAtLeast100Felt(dataitem):
    if dataitem["properties"]["felt"] is None or dataitem["properties"]["felt"] < 100:
        return False
    return True

print(f"Total quakes: {len(data['features'])}")
atLeast100 = list(filter(getAtLeast100Felt, data['features']))
print(f"Total quakes felt by at least 100 people: {len(atLeast100)}")


def getFelt(dataitem):
    return dataitem["properties"]["felt"]


theMost = max(atLeast100, key=getFelt)
print(f"Most felt reports: M {theMost['properties']['mag']} - {theMost['properties']['place']}",
      f", reports: {theMost['properties']['felt']}")

def getSig(dataitem):
    if dataitem["properties"]["sig"] is None:
        return 0
    return dataitem["properties"]["sig"]

mostSig = sorted(data['features'], key=getSig, reverse=True)
for i in range(0, 10):
    print(f"Event: M {mostSig[i]['properties']['mag']} - ",
          f"{mostSig[i]['properties']['place']}: ",
          mostSig[i]['properties']['sig'])
