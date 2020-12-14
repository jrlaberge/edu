#!/usr/local/bin/python3
#
# Prints a list of students in a given house, in alphabetical order
# Program will take only 1 argument (house name)
# The output should be formatted as such:
# {first_name} {middle_name} {last_name} born {year}
#
# the output should be sorted by last name, in the event of duplicate last name, it should be then sorted by first name
# null should not be printed

import cs50
import sys

# Connect to DB; students.db
db = cs50.SQL('sqlite:///students.db')

houses = []
query = db.execute('select distinct house from students')
for house in query:
    houses.append(house['house'])


def get_roster(house):
    raw_roster = db.execute("select first, middle, last, birth from students where house = ? order by last, first", house)
    for student in raw_roster:
        first_name = student['first']
        middle_name = student['middle']
        last_name = student['last']
        birth_year = student['birth']

        if middle_name == None:
            print(f"{first_name} {last_name}, born {birth_year}")
        else:
            print(f"{first_name} {middle_name} {last_name}, born {birth_year}")


if __name__ == '__main__':

    # Validate that 1 argument is supplied.
    if len(sys.argv) != 2:
        print("Usage: ./roster.py <house name>")
        sys.exit(1)

    house = sys.argv[1]

    if house not in houses:
        print("I don't know what you're asking me. Are you a Muggle?")
        sys.exit(2)

    get_roster(house)