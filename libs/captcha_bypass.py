from selenium import webdriver
import requests
import time
import random
import json
import webbrowser
from termcolor import colored
from datetime import datetime

def cprint(*args, end_each=" ", end_all=""):
	dt = str(datetime.fromtimestamp(int(time.time())))
	print(colored(dt, "white"), end=end_each)
	for i in args:
		print(colored(str(i[0]), i[1].lower()), end=end_each)
	print(end_all)


def captchasolve(captcha_id = str):
    pageurl = captcha_id

    try:
        webbrowser.open_new(pageurl)
        input()
        return
        
    except:
        print("IDK how you messed that one up, chief :/")
        return "Chrome"
