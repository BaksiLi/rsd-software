import csv


def csv_read(csvfile):
    """Reads a CSV file.

    Args:
        CSV file name as string.

    Return:
        A list of lists of floats.
    """
    f = csv.reader(csvfile, delimiter=',', quotechar='|')
    number_columns = []
    for i, row in enumerate(f):
        number_columns.append([])
        for number in row:
            number_columns[i].append(float(number))
    return number_columns


<<<<<<< HEAD
def csv_write():
    pass
=======
def csv_write(file_name, result):
    with open("output.csv", "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(result)
    
>>>>>>> fbb2bd53676d45723da76bd222772a24eee4b5c5
