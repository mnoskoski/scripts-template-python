#!/usr/bin/env python
import datetime
import json
import logging
import os 
import sys

#args
json_file_dates= sys.argv[1]

#init agent log
logging.basicConfig(
    format="[%(asctime)s] [%(levelname)s] - %(message)s",
    datefmt="%d-%m-%Y %I:%M:%S",
    level=logging.DEBUG
)

##functions
def read_freezing_dates(json_file):
    try:
        with open(json_file_dates) as file:
            data = json.load(file)
    except FileNotFoundError:
        logging.error("File not Found")
        data = None
    except Exception as e:
        logging.error(f"An error Occurred: {e}")
        data = None
    return data

def compare_dates():
    var = "freezing_dates" #botei esse flag só pra testar a var dentro do get 
    freezing_time = read_freezing_dates(json_file_dates)
    start_date = freezing_time.get(var, {}).get("start") #
    end_date = freezing_time.get("freezing_dates").get("end")
    print(f"Start Date: {start_date}, \nEnd Date: {end_date}\n")
    if datetime.date.today() >= datetime.date.fromisoformat(start_date) and datetime.date.today() <= datetime.date.fromisoformat(end_date):
        print("::warning::We are in the freezing period")
        sys.exit(1)
    else:
        print("We are not in the freezing period")

compare_dates()
