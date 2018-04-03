"""Parse log entries for datetimes and calculate the time
   between two shutdown initializations"""
from datetime import datetime
import os
import urllib.request
import sys

def read_file():
    """Read in tempfile return list of lines"""
    with open('log.txt', 'r') as f:
        log_lines = f.readlines()
        return(log_lines)
    pass


def convert_to_datetime(line):
    """Given a line extract timestamp and convert to datetime"""
    if str(line).startswith('INFO '):
        extract_date_time = line[5:24]
        return datetime.strptime(extract_date_time, '%Y-%m-%dT%H:%M:%S')
    elif str(line).startswith('ERROR '):
        extract_date_time = line[6:25]
        return datetime.strptime(extract_date_time, '%Y-%m-%dT%H:%M:%S')
    pass


def time_between_shutdowns(lines):
    """Extract shutdown init events and calculate timedelta between
       first and last one"""
    list_of_shutdown_inits = []
    for l in lines:
        if 'Shutdown initiated' in l:
            time_date_shutdown = convert_to_datetime(l)
            list_of_shutdown_inits.append(time_date_shutdown)
    print(list_of_shutdown_inits)
    #first_shutdown_init = convert_to_datetime(list_of_shutdown_inits[0])
    #last_shutdown_init = convert_to_datetime(list_of_shutdown_inits[1])
    print(list_of_shutdown_inits[1]-list_of_shutdown_inits[0])
    pass

#read_file()
#convert_to_datetime(read_file())
time_between_shutdowns(read_file())

