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


def csv_write():
    pass
