# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperature = int(row[1])
#             temperatures.append(temperature)
#
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)


# temp_list = data["temp"].to_list()
#
# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #Get Data in Columns
# print(data["condition"])
# print(data.condition)

#Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
#
# monday_temp = int(monday.temp)
#
# monday_temp_F = (monday_temp * 9/5) + 32
#
# print(monday_temp_F)

#Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]
fur_color_list = fur_color.to_list()

gray = 0
red = 0
black = 0

for color in fur_color_list:
    if color == 'Gray':
        gray += 1
    if color == 'Cinnamon':
        red += 1
    if color == 'Black':
        black += 1

fur_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray, red, black]
}

squirrel_data = pandas.DataFrame(fur_dict)
print(squirrel_data)

squirrel_data.to_csv("squirrel_count.csv")




