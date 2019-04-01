#Program to read a csv file data in a for loop.

import csv

fileopen = open('example_1.csv')
filereader = csv.reader(fileopen)
for row in filereader:
     print('Row #' + str(filereader.line_num) + ' ' + str(row))
