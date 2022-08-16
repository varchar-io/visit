# the main logic of visit
import os
import sys

USAGE = """
Usage:
  visit <file.csv>
"""
RESULT = """
URL: https://columns.ai/visual/xyz/abc?temp
"""
if len(sys.argv) < 2:
    print(USAGE)
    sys.exit()

input_file = sys.argv[1]

if not os.path.exists(input_file):
    print("The specified file does not exist")
    sys.exit()

print(RESULT)
