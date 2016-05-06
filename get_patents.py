#!/usr/local/bin/python3

""" 
Patent analysis on patents related to prediction, data analysis, big data,
artificial intelligence, and machine learning.

Uses Google Search API to collect patents from google.com/patents according
to specific keywords. Returns patents in JSON format.

"""

import requests
import urllib
import time
import json
import sys
from jsonmerge import merge
from pprint import pprint

# Get your own access token and custom search engine id (cse_id) from Google.
access_token = "AIzaSyDbqANZ1QHg-V_gBK7EP8iPWVCeTun20Dc"
cse_id = "000401063296163684824:-zjnv7z7vhu"

# Check for user args.
if (len(sys.argv) > 1):
    search_text = ""

    for arg in sys.argv[2:len(sys.argv)]:
        if (search_text == ""):
            search_text = str(arg)
        else:
            search_text = str(search_text + "+" + arg)

    end = int(sys.argv[1])
else:
    print("<number> <tag> <tag> ...")
    sys.exit()


# Build URL.
num = "10"
for i in range(1, end):
    start = str(i)
    url = "https://www.googleapis.com/customsearch/v1?" + \
          "key=" + access_token + \
          "&cx=" + cse_id + \
          "&start=" + start + \
          "&num=" + num + \
          "&tbm=pts" + \
          "&q=" + search_text

    # Request data from Google Patents.
    response = requests.get(url)
    response.json()

    # Write the response to a file.
    f = open(search_text + "_" + "{:02d}".format(i) + ".json", "w")
    f.write(json.dumps(response.json(), indent = 2))
    f.close()

    # Sleep for 1 second, API request limit.
    time.sleep(1) 

# Merge the separate files into one file with one JSON object.

