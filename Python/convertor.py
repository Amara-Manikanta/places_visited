import csv
import json


file="places.xlsx"
data=[]
with open("E:\Manikanta\Places_visited\places_visited\Python\places.csv",encoding='cp1252') as cvsf:
    csvreader = csv.DictReader(cvsf)
    for row in csvreader:
        data.append(row)

with open(r"E:\Manikanta\Places_visited\places_visited\States\andhrapradesh.json", "w") as outfile:
    json.dump(data, outfile,indent=4)

print(data)