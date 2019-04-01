# Program to write data to csv file.

import csv

File = open('example_2.csv', 'w')
Writer = csv.writer(File)

Writer.writerow(['Name', 'Age', 'Rank'])
Writer.writerow(['Nick', 11, 3])
Writer.writerow(['Chris', 13, 1])
Writer.writerow(['Mark', 10, 2])

File.close()
