#!/usr/bin/env python3

import os
import requests
from glob import glob
import reports
import emails
from datetime import datetime


def process_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        file_dict = {"name": lines[0].strip(), "weight": int(lines[1].strip().replace(' lbs', '')), "description": lines[2].strip(), "image_name": filename.split('/')[3].replace('txt', 'jpeg')}
        f.close()
    return file_dict

def get_files(file_path, ext):
    files = glob("{}*.{}".format(file_path, ext))
    return files

if __name__ == '__main__':
    files = get_files('./supplier-data/descriptions/', 'txt')
    file_list = []
    paragraph = ''
    for f in files:
        file_list.append(process_file(f))
    for f in file_list:
        response = requests.post('http://localhost/fruits/', json=f)
        print(response.status_code)
        paragraph += "name: {}<br />weight: {} lbs<br />".format(f["name"], f["weight"])

    title = "Processed Update on {}".format(datetime.now().strftime('%B %d, %Y'))
    reports.generate_report('/tmp/processed.pdf', title, paragraph)

    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)

