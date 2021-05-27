# with open("weather_data.csv") as f:
#     data = f.readlines()
# print(data)

import csv

with open("weather_data.csv") as f:
    data = csv.reader(f)
    for row in data:
        print(row)