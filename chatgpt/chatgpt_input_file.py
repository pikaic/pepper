#! /home/logan_18/anaconda3/envs/pepperenv/bin/python3
# -*- encoding: UTF-8 -*-


import openai
import json

#this is the api key
openai.api_key="your api key"
question=input("Enter your question: ")
completion=openai.Completion.create(engine="text-davinci-003",prompt=question,max_tokens=1000)
response=completion.choices[0]['text']



#writing the output to a json file
sorted_output=json.dumps(response)
with open('json_file.json', "w") as outfile:
    outfile.write(sorted_output)