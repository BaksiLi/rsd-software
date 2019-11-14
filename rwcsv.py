import csv


def csv_read(file_name):
    """Reads a CSV file.

    Args:
        CSV file name as string.

    Return:
        A list of lists of floats.
    """
    with open(file_name, 'rb') as csvfile:
        f = csv.reader(csvfile, delimiter=',', quotechar='|')
        number_columns = [list([]) for _ in range(len(next(f)))]
        for row in f:            
            for i, number in enumerate(row):
                number_columns[i].append(float(number))
    return number_columns


def csv_write(file_name, result):
    with open(file_name, "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(result)
    
