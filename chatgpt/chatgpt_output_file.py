#! /usr/bin/python2
# -*- encoding: UTF-8 -*-

import naoqi
from naoqi import ALProxy
import json

# PEPPER_IP="192.168.178.47"
# PORT=9559

# fetching the data from the json file
json_data=open('/home/logan_18/pepper/chatgpt/json_file.json')
data=json.load(json_data)


# data fetched from the json file is in unicode format which is then converted to string for pepper to recognize
data_string=data.encode()


# calling pepper's text to speech API 
# test=ALProxy("ALTextToSpeech",PEPPER_IP,PORT)
# test.say(data_string)


print(data_string)