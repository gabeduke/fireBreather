#!usr/bin/env python
import smtplib
from properties import *
from ISStreamer.Streamer import Streamer
import requests
import json
import logging


# # Enable Logging # #
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


def get_wio_sensor_data(node, token):
    l = []
    for x in range(0, 3):
        req = requests.get(wio_url + node.value + token)
        print "Query Response: " + str(req.status_code) + " " + req.content

        resp_dict = json.loads(req.content)  # loads the request into a dictonary for parsing
        sensor_data = resp_dict[node.name]  # parses the value from the request dictionary

        l.append(sensor_data)

    print(l)
    return mean(l)

