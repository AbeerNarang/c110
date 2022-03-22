import csv
import random 
import pandas as pd
import plotly_express as px
import plotly.figure_factory as ff
import statistics 

v1 = pd.read_csv("data.csv")
data = v1["temp"].tolist()
mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
graph = ff.create_distplot([data], ["temp"], show_hist = False)
graph.show()
print("Mean: ",mean)
print("Median: ",median)
print("Mode: ",mode)

dataset = []
for i in range(0,100):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)

mean2 = statistics.mean(dataset)
graph2 = ff.create_distplot([dataset], ["temp"], show_hist = False)
graph2.show()