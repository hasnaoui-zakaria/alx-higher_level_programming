#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
and displays the body of the response in a specific format.
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)
    content = response.text

    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    
