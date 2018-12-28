from django.shortcuts import render
from django.http import JsonResponse
import configparser
import os

basepath = os.path.dirname(os.path.abspath(__file__))
config = configparser.ConfigParser()
config.read(os.path.join(basepath, 'config.ini'))


def show_logs(request):
    logs = {"logs": [line for line in get_logs()]}
    return JsonResponse(logs)


def get_logs():
    with open(config["CUSTOMLOGPATH"], "r") as log_file:
        for line in log_file:
            yield line

