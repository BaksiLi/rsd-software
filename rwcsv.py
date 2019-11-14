import csv

def csv_read(csvfile):
    csv.reader(csvfile, delimiter=',', quotechar='|')

def csv_write():
    