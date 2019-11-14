from argparse import ArgumentParser
from average import average
from rwscv import csv_write, csv_read

if __name__ == "__main__":
    """
    The entrypoint for the column averaging software suite.
    """
    parser = ArgumentParser(description="Give it a input csv")
    parser.add_argument("inputcsv")
    parser.add_argument("outputcsv")
    arguments = parser.parse_args()
    data_columns = csv_read(arguments.inputcsv)
    average_columns = average(data_columns)
    write_csv = csv_write(average_columns)