#!/usr/bin/env python3
import socket
import psutil
import emails
import os

def get_cpu():
    return psutil.cpu_percent()
def get_used_disk_space():
    return psutil.disk_usage('/').percent
def get_available_memory():
    return (psutil.virtual_memory().free / 1024) / 1024
def resolve_localhost():
    return socket.gethostbyname('localhost') == '127.0.0.1'

if __name__ == '__main__':
    if not resolve_localhost():
        error = "Error - localhost cannot be resolved to 127.0.0.1"
    elif get_available_memory() < 500:
        error = "Error - Available memory is less than 500MB"
    elif get_used_disk_space() > 80:
        error = "Error - Available disk space is less than 20%"
    elif get_cpu() > 0.8:
        error = "Error - CPU usage is over 80%"
    if error:
        body = "Please check your system and resolve the issue as soon as possible."
        sender = "automation@example.com"
        receiver = "{}@example.com".format(os.environ.get('USER'))
        subject = error
        message = emails.generate_email(sender, receiver, subject, body)
        emails.send_email(message)


