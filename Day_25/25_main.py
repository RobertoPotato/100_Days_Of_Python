# # import csv
# #
# # with open('weather_data.csv') as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #
# #     print(temperatures)
#
# import pandas
# # table is Dataframe object
# # columns are Series object
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(type(data["temp"]))
#
# # data_dict = data.to_dict()
# # # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# # print(temp_list)
# #
# # max_ = data["temp"].max()
# # print(max_)
#
# # day = data[data.temp == data.temp.max()]
# # print(day)
#
# monday = data[data.day == "Monday"]
# print((monday.temp * (9/5) + 32))
#
# # Create a df from scratch
#

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data["Primary Fur Color"])

len_g = len(data[data["Primary Fur Color"] == "Gray"])
len_r = len(data[data["Primary Fur Color"] == "Cinnamon"])
len_b = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len_g, len_r, len_b]
}

print(data_dict)
df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
