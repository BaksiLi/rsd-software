import csv

def csv_read(csvfile):
    csv.reader(csvfile, delimiter=',', quotechar='|')

def csv_write(file_name, result):
    with open("output.csv", "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(result)
    
