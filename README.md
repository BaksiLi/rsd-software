# rsd-software

## Program overview

- Read CSV file of numbers formatted in columns.
- Take average of the columns.
- Write CSV file of the averages.

## Program structure 

- Main guard as entrypoint for program.
- Read CSV function and returns a list of lists in `csvrw.py`.
- Averaging function which averages every list in a list and returns a list of averages.
- Write function in `csvrw.py` which writes a CSV that contains a list of averages corresponding to the columns in the input data CSV file.