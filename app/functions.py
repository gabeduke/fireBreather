#!usr/bin/env python
from properties import *
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
    req = requests.get(wio_url + node.value + token)
    print "Raw Query Response: " + str(req.status_code) + " " + req.content

    resp_dict = json.loads(req.content)  # loads the request into a dictonary for parsing
    return resp_dict[node.name]  # parses the value from the request dictionary


def get_temperature(token):
    raw = get_wio_sensor_data(NodeProperties.temperature, token)
    Fahrenheit = 9.0/5.0 * raw + 32
    print("\nConverting raw response to Fahrenheit ...")
    print("Fahrenheit temperature is : " + str(Fahrenheit))
    raw_input("\n\nPress Enter to continue...")
    return Fahrenheit
