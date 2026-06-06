# create a program by python to login to a website in bash

import requests
import json
import os
import sys
import time
import random
import string
import datetime
import threading
import subprocess

def login(username, password):
    url = "https://www.google.com"
    response = requests.get(url)
    print(response.text)

if __name__ == "__main__":
    login("username", "password")
    login("username", "password")
    login("username", "password")       


    
