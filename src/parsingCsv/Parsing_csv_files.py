# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    i = 0
    keys = None
    with open(datafile, "r") as f:
        while (True):
            if i == 11:
                break
            line = f.readline()

            if i == 0:
                keys = [key.strip() for key in line.split(',')]
            else:
                values = [value.strip() for value in line.split(',')]
                my_entry = dict(zip(keys, values))

                data.append(my_entry)
            i += 1
        return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)',
                 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum',
                 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964',
                 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    if d[0]==firstline:
        print("First Asertion True")
    assert d[9] == tenthline
    if d[9]==tenthline:
        print("Second assertion true")


test()
