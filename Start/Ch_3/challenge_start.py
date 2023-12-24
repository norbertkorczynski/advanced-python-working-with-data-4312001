# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime


# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD

headers = ["Magnitude", "Place", "Felt Reports", "Date", "Link"]
rows= []

def getSig(quake):
    sig = quake["properties"]["sig"]
    return sig if sig is not None else 0

sortedData = sorted(data["features"], key=getSig, reverse=True)
sortedMostSigData = sorted(sortedData[0:40], key=lambda q: q["properties"]["time"], reverse=True)

for quake in sortedMostSigData:
    thedate = datetime.date.fromtimestamp(
        int(quake["properties"]["time"]/1000))
    rows.append([quake["properties"]["mag"],
                quake["properties"]["place"],
                quake["properties"]["felt"],
                thedate,
                f'''https://www.google.com/maps/search/?api=1&query='''
                    f'''{quake["geometry"]["coordinates"][1]}%2C'''
                    f'''{quake["geometry"]["coordinates"][0]}'''
                ])


with open("significantevents.csv", "w", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(headers)
    writer.writerows(rows)
