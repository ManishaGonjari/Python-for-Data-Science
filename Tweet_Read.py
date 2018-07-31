# -*- coding: utf-8 -*-
"""
@author: UTD
"""

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json


# Keeping blank due to security issue
consumer_key=''
consumer_secret=''
access_token =''
access_secret=''


class TweetsListener(StreamListener):

  def __init__(self, csocket):
      self.client_socket = csocket

  def on_data(self, data):
      try:
          msg = json.loads( data )
          print( msg['text'].encode('utf-8') )
          self.client_socket.send( msg['text'].encode('utf-8') )
          return True
      except BaseException as e:
          print("Error on_data: %s" % str(e))
      return True

  def on_error(self, status):
      print(status)
      return True

def sendData(c_socket):
  auth = OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_secret)

  twitter_stream = Stream(auth, TweetsListener(c_socket))
  inp = input('Enter input for analysis')
  twitter_stream.filter(track= inp)

if __name__ == "__main__":
  s = socket.socket()         # Creating socket object
  host = "127.0.0.2"          # local machine
  port = 5555                 # Port
  s.bind((host, port))        # port binding

  print("Listening on port: %s" % str(port))

  s.listen(5)                 # Waiting for client connection.
  c, addr = s.accept()        # Connection with client.

  print( "Received request from: " + str( addr ) )

  sendData( c )
