#-*-coding:utf-8-*-

import sys
import random
import string

import csv
import pandas as pd
from pandas import Series, DataFrame
import json
# Papago API
import os
import sys
import urllib.request

def get_transtlated_string(oriString) :
  lists = list()
  df = pd.read_csv('computer+science+jargon.csv', index_col=False, names=['words'], dtype = {"words" : str})  
  df['count_blank'] = df.words.str.count(' ')
  df.sort_values(by=['count_blank'], ascending=False, inplace=True)

  # Replace with a word that cannot be translated
  index = -1
  lowerString = oriString.lower()
  for i in df['words']:
      stIndex = -1
      while True :
          stIndex += 1
          stIndex = lowerString.find(i.lower(), stIndex)
          # there is no specific words
          if stIndex == -1 :
              break
          edIndex = len(i) + stIndex
          if (stIndex == 0 or lowerString[stIndex - 1].isalnum() == False) and (edIndex == len(lowerString) or lowerString[edIndex].isalnum() == False):
              #replace
              lists.append(oriString[stIndex:edIndex])
              index += 1
              afterChange = "A" + str(index) + "A"
              oriString = oriString[:stIndex] + oriString[edIndex:]
              oriString = oriString[:stIndex] + afterChange + oriString[stIndex:]
              lowerString = lowerString[:stIndex] + lowerString[edIndex:]
              lowerString = lowerString[:stIndex] + afterChange + lowerString[stIndex:]

  # Papago API
  client_id = "GRuteQ_VyvUQq3YAo2JC" # 개발자센터에서 발급받은 Client ID 값
  client_secret = "VuKO2bhlLl" # 개발자센터에서 발급받은 Client Secret 값
  encText = urllib.parse.quote(lowerString)
  data = "source=en&target=ko&text=" + encText
  url = "https://openapi.naver.com/v1/papago/n2mt"
  request = urllib.request.Request(url)
  request.add_header("X-Naver-Client-Id",client_id)
  request.add_header("X-Naver-Client-Secret",client_secret)
  response = urllib.request.urlopen(request, data=data.encode("utf-8"))
  rescode = response.getcode()
  if(rescode==200):
      response_body = response.read()
      # Replace with original language
      res = json.loads(response_body.decode('utf-8'))
      translatedString = res['message']['result']['translatedText']
      for i in range(index + 1) :
        afterChange = "A" + str(i) + "A"
        translatedString = translatedString.replace(afterChange, lists[i])
  else:
      translatedString = "Error Code:" + rescode
  return translatedString


def get_random_string(length):
  word = string.ascii_lowercase
  result = ''.join(random.choice(word) for i in range(length))
  return result

if len(sys.argv) <= 1 :
  print("ERROR : Please enter the string data")
else :
  inputString = ' '.join(sys.argv[1:])
  if len(inputString) > 5000 :
    print("ERROR : Please enter string data of less than 5000 characters.")
  else :
    outputString = get_transtlated_string(inputString)
    print(outputString)

  # str_length = len(sys.argv[1])
  # print(get_random_string(str_length))