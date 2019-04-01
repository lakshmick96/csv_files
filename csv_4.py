# Program to write data to a CSV file with the delimiter and line terminator arguments.(Here cells are separated by tabs. Hence using the file extension .tsv, for tab-separated values.)

import csv
csvFile = open('example_3.tsv', 'w', newline='')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
csvWriter.writerow(['apples', 'oranges', 'grapes'])
csvWriter.writerow(['eggs', 'bacon', 'ham'])
csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
csvFile.close()
