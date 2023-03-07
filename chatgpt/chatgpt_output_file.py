#! /usr/bin/python
# -*- encoding: UTF-8 -*-

import naoqi
from naoqi import ALProxy
import json

json_data=open('json_file.json')
data=json.load(json_data)


data_string=data.encode()


test=ALProxy("ALTextToSpeech","169.254.102.67",9559)
test.say(data_string)
