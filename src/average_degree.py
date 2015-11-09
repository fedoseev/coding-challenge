# example of program that calculates the average degree of hashtags
# To Do:
# Extract hashtags and timestamp from each tweet


import io
import os
import sys
import json
import codecs
import string
import networkx as nx #sudo pip install networkx
import igraph as ig #sudo pip install igraph
#import future  # requires pip install
from os import path



def main():

  RAW_TWEETS_FILE = sys.argv[1]
  AVERAGE_DEGREE_TWEETS_FILE = sys.argv[2]
  tweets_with_hashtags = 0
  tweetscount = 0
  twitter_hashtag_list = []
  
  
  hashtaglist = []

  with io.open(RAW_TWEETS_FILE, encoding='utf-8') as f:
    

    print('\nStarting the second part of the challenge')
    
    G = nx.Graph()
    gr = ig.Graph()  
    
    if path.isfile(AVERAGE_DEGREE_TWEETS_FILE):
       try:
          os.remove(AVERAGE_DEGREE_TWEETS_FILE)
       except OSError:
          pass
    fout = open(AVERAGE_DEGREE_TWEETS_FILE,"a+",)

    for line in f:
      tweet = json.loads(line)    
      
      # Checking if that is  a valid tweet:
      if 'text' in tweet:
        tweetscount +=1 #Debugging
      # Extractting data from the tweet
        
        hashtags = tweet["entities"]["hashtags"] # Creating a preliminary list of hashtags
        
        hashtaglist = []
        for ht in hashtags:
          if ht != None:
            hashtaglist.append(ht["text"].encode("ascii", "ignore")) # Creating a list of valid tweets
             
        if len(hashtaglist) > 1:
           
           # Creating edges to insert into the graph
           edges = [hashtaglist[i]+','+hashtaglist[i+1] for i in range(len(hashtaglist)-1)]
           #G.add_edges_from[edges] 


    fout.close()
    
if __name__ == "__main__":
  main()
