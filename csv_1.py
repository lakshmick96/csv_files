#Program to read a csv file.

import csv

fileopen = open('example_1.csv')
filereader = csv.reader(fileopen)
data = list(filereader)
print(data)

