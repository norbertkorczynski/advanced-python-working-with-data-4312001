# Example file for Advanced Python: Working With Data by Joe Marini
# read data from a CSV file into an object structure

import csv
import pprint

#header = ["Place", "Magnitude", "Link", "Date"]
# read the contents of a CSV file into an object structure
result = []

#Place,Magnitude,Link,Date
# open the CSV file for reading
with open("largequakes.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    sniffer = csv.Sniffer()
    sample = csvfile.read(1024)
    csvfile.seek(0)

    if sniffer.has_header(sample):
        next(reader)

    for row in reader:
        #print(row)
        result.append(
            {
            "place": row[0],
            "mag": row[1],
            "url": row[2],
            "date": row[3]
            })

pprint.pp(result)
