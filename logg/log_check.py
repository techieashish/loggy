import configparser
import os
import time
import datetime

basepath = os.path.dirname(os.path.abspath(__file__))
config = configparser.ConfigParser()
config.read(os.path.join(basepath, 'config.ini'))

last_updated = datetime.datetime.now()
seek_from = 0


def main():
    parse_once()
    while True:
        copy_logs()
        time.sleep(60)


def copy_logs():
    global last_updated, seek_from
    last_modified = os.path.getmtime(config["MainLOGPath"])
    if datetime.datetime.fromtimestamp(last_modified) > last_updated:
        with open(config["MainLOGPath"], "r") as ml:
            ml.seek(seek_from) # Read the main log file from where it stopped last time.
            current_last_n_lines = ml.readlines()
            seek_from = ml.tell() # Updating the last stopped.
        with open(config["CUSTOMLOGPATH"], "r") as lf:
            data = lf.readlines() # Getting all the logs from the custom log file in order to maintain only 100 logs.
        with open(config["CUSTOMLOGPATH"], "w") as lfout:
            lfout.write(data[len(current_last_n_lines):])
            for line in current_last_n_lines:
                lfout.write(line)
        last_updated = last_modified


def parse_once():
    global seek_from
    with open(config["MainLOGPath"], "rb") as log_file:
        log_file.seek(seek_from, os.SEEK_END)
        fsize = log_file.tell()
        log_file.seek(max(fsize - 1024, 0), 0)
        lines = log_file.readlines()
        seek_from = log_file.tell()
    fl = open(config["CUSTOMLOGPATH"], "w")
    for line in lines[-100:0]:
        fl.write(line)
    fl.close()



