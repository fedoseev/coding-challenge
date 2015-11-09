# My implementation of the coding challenge
# -*- coding: UTF-8 -*-
# TO DO:
# Identify Non ASCI codes in UNICODE string

import io
import os
import sys
import json
import codecs
import string

#import future  # requires pip install
from os import path

def isUnicode(s): # 
  # if encode and decode equals the original
  # than it doesnt have special characters
  encoded_text = s.encode("ascii", "ignore")
  decoded_text = encoded_text.decode('utf-8')
  if decoded_text == s:
    return False
  return True
  
if __name__ == "__main__":
   

  #0.1 input parameters
  RAW_TWEETS_FILE = sys.argv[1]
  CLEANED_TWEETS_FILE = sys.argv[2]
  
  with io.open(RAW_TWEETS_FILE,encoding='utf-8') as f:    
    Unicode_Tweets_Count = 0;    
    
    raw_tweet_text = ""
    created_at_text = ""
    if path.isfile(CLEANED_TWEETS_FILE):
       try:
          os.remove(CLEANED_TWEETS_FILE)
       except OSError:
          pass
      
    fout = open(CLEANED_TWEETS_FILE,"a+",)
    print('Starting the first part of the challenge')
    
    for line in f:
      tweet = json.loads(line)
      #1.1 Extract text from the tweet
      
      # Checking if that is  a valid tweet:
      if 'text' in tweet:
          
        raw_tweet_text = tweet['text']
        raw_tweet_text = raw_tweet_text.replace('\n', ' ')
        raw_tweet_text = raw_tweet_text.replace('\t', ' ')

        encoded_tweet_text = raw_tweet_text.encode("ascii", "ignore")
        no_white_space_tweet = encoded_tweet_text.strip()

        if  isUnicode(raw_tweet_text):
            Unicode_Tweets_Count +=1
        
      #1.3 Extract timestamp: 
        timestamp_text = " (timestamp: " + tweet['created_at']  + ")"
       
        fout.write(no_white_space_tweet + timestamp_text + "\n")
        
  # close the file when done
  fout.write('\n' + str(Unicode_Tweets_Count) + " tweets contained unicode")
  fout.close()
  
  #print "the file had " + str(linecount) + " tweets" # DEBUG LINE
  #print str(Unicode_Tweets_Count) + " tweets contained unicode" # DEBUG LINE
  