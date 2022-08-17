# the main logic of visit
import os
import sys
import requests
import webbrowser

from models import VisitRequest

HOST = "https://columns.ai"
DEV_HOST = "http://localhost:8088"
SERVER = DEV_HOST + "/api/sdk/visit"
APIKEY = "public"
USAGE = """
Visit = Visualize It
Usage:
  visit <file.csv>

Use a sample csv:
  https://github.com/varchar-io/visit/raw/main/gdp-state.csv
"""

RESULT = """
Visit URL: {0}
"""

if len(sys.argv) < 2:
    print(USAGE)
    sys.exit()

input_file = sys.argv[1]

if not os.path.exists(input_file):
    print("The specified file does not exist")
    sys.exit()

# upload the file to Columns and create a data set
# build a request as JSON object
# {apiKey: string, key: string, data: string, format: csv, headless: false}
# then post it to "columns.ai/api/sdk/visit" to get the URL
req = VisitRequest(APIKEY)
req.key = os.path.basename(input_file)
print("Visualizing " + req.key)

# read the file and set the content
with open(input_file) as f:
    req.data = f.read()
    f.close()

# check if the request is valid
if len(req.data) == 0:
    print("The specified file is empty")
    sys.exit()

# make the call
print("Contacting " + HOST)
reply = requests.post(SERVER, json=req.toJson())
if not reply.ok:
    print("Failed to contact " + HOST)
    sys.exit()

url = reply.text
if not url.startswith(HOST):
    print("Failed to get a visualizer")
    sys.exit()

# tell user the final result
print(RESULT.format(url))

# use web browser to open it
webbrowser.open(url, new=2)
