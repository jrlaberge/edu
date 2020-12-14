#!/usr/local/bin/python3

# import data from a CSV spreadsheet into an sqllite db
# accept a csv filename as cli argument
# return an error message and exit if incorrect number of arguments are given
#
# Assumptions
#   CSV passed through CLI arguments is valid
#   CSV will have columns: name, house and birth
#   If name contains 2 spaces, it will have a first and last name, if it contains 3 spaces it will also contain a middle name
#   If no middle name, insert NULL
import csv
import cs50
import sys
from pathlib import Path

# connect to DB
db = cs50.SQL('sqlite:///students.db')
db.execute('DELETE FROM students')


def load_csv(csv_file):
    with open(csv_file, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        students = {}
        for row in reader:
            name = row['name'].split(' ')

            # If there is 2 names (meaning only 1 white space), we assume there is no middle name so we fill in NULL
            if len(name) == 2:
                first_name = name[0]
                middle_name = None
                last_name = name[1]
            # If there is 3 names (meaning 2 white spaces), we assume there is a middle name. Anything else is not inserted.
            elif len(name) == 3:
                first_name = name[0]
                middle_name = name[1]
                last_name = name[2]

            house = row['house']
            birth = row['birth']

            db.execute("INSERT into students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                       first_name,
                       middle_name,
                       last_name,
                       house,
                       birth
                       )


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./import.py <path-to-csv-file")
        sys.exit(1)

    csv_file = Path(sys.argv[1])

    # Validate that CSV file exists
    if not csv_file.exists():
        print(f"{csv_file} does not exist or is not accessible.")
        sys.exit(2)

    load_csv(csv_file)