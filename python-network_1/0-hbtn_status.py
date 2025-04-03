#!/usr/bin/python3
import urllib.request

url = "https://alu-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print("Body response:")
        print("\t- {}".format(body))
except urllib.error.URLError as e:
    print(f"Error fetching URL: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")