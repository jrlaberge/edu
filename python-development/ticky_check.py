#!/usr/bin/env python3

import re
import operator
import csv

error = {}
per_user = {}

with open('./syslog.log', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        error_type = re.search(r'ERROR(.+?)\(', line)
        if error_type:
            error_type = error_type.group(1).strip()
        if re.search(r"ticky: ERROR ([\w ]*) " , line):
            if error_type in error:
                error[error_type] += 1
            else:
                error.update({error_type: 1})

        user = re.search(r'\((.+?)\)', line)
        if user:
            user = user.group(1).strip()
        else:
            user = "unknown_user"
        if user in per_user:
            if re.search(r"ticky: ERROR", line):
                per_user[user][1] += 1
            elif re.search(r"ticky: INFO", line):
                per_user[user][0] += 1
        else:
            if re.search(r"ticky: ERROR", line):
                per_user.update({user: [0, 1]})
            elif re.search(r"ticky: INFO", line):
                per_user.update({user: [1, 0]}) 
    file.close()

with open('error_message.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Error", "Count"])
    for e, count in sorted(error.items(), key=operator.itemgetter(1), reverse=True):
        writer.writerow([e, count])
    file.close()

with open('user_statistics.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Username", "INFO", "ERROR"])
    for user, count in sorted(per_user.items(), key=operator.itemgetter(0)):
        writer.writerow([user, count[0], count[1]])
    file.close()

