#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.

Usage: ./6-post_email.py <URL> <email>

- Displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./6-post_email.py <URL> <email>")
    else:
        url = sys.argv[1]
        value = {"email": sys.argv[2]}
        try:
            r = requests.post(url, data=value)
            r.raise_for_status()  # Handle HTTP errors gracefully
            print(r.text)
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
