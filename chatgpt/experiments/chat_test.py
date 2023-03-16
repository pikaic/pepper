#! /home/logan_18/anaconda3/envs/peppercudaenv/bin/python3
# -*- encoding: UTF-8 -*-



import whisper
import openai
import json
import pyaudio
import wave
import os
import functools


def chatgpt_response(question):

    openai.api_key="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"
    conversation=[{"role":"system","content":"You are a helpful assistant"}]

    while(1):
        conversation.append({"role":"user","content": question})
        response=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation,
            temperature=0.2,
            max_tokens=1000,
            top_p=0.9
        )

        conversation.append({"role":"assistant","content":response['choices'][0]['message']['content']})
        answer=response['choices'][0]['message']['content']
        print("\n" + answer + "\n")


        confirmation=input("Do you wish to continue asking questions? Say yes or no please.")
        if(confirmation=="yes" or confirmation=="YES"):
            continue
        elif(confirmation=="no" or confirmation=="NO" or confirmation=="nO" or confirmation=="No"):
            break



