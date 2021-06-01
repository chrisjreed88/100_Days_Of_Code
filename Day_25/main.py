"""Open file and read data"""
# with open("weather_data.csv") as f:
#     data = f.readlines()
# print(data)

"""Using standard CSV library"""
# import csv

# with open("weather_data.csv") as f:
#     data = csv.reader(f)
#     for row in data:
#         print(row)

"""Using Pandas Library"""

# data = pandas.read_csv("weather_data.csv")
"""Convert data to another format"""
# data_dict = data.to_dict()
# print(data_dict)

"""Get average temperature"""
# temp_list = data["temp"].to_list()
# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)

"""built in mean method"""
# avg_temp = data["temp"].mean()
# print(avg_temp)

"""Get data from a row"""
# print(data["temp"].max())
# print(data[data.temp == data.temp.max()])

"""Convert temp to farenheit"""
# monday = data[data.day == "Monday"]
# temp_farenheit = (monday.temp * 9/5) + 32
# print(temp_farenheit)

"""Create pandas data frame"""
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data_frame = pandas.DataFrame(data_dict)

"""write out to csv file"""
# data_frame.to_csv("new_data.csv"

"""Squirrel Data"""
import pandas
squirrel_data = pandas.read_csv(
    "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
red_squirrels = len(
    squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(
    squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
gray_squirrels = len(
    squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
squirrel_colour_data = pandas.DataFrame({
    "Fur Colour": ["grey", "red", "black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels]
})
squirrel_colour_data.to_csv("new_squirrel_data.csv")
