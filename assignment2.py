#!/usr/bin/python

import struct
import sys
import pwd
import os
import time
import sqlite3

################################################
#           user logins
################################################
def wtmp_read():
  # Call 'last' through bash (sad face!)
  with os.popen("last") as f:
    data = f.read()
  return data.split('\n')[:-2]

def wtmp_parse(args):
  # If no user was specified
  if len(args) == 0:
    for i in wtmp_read():
      print i
  # If a user was specified, only report records for them
  elif len(args) == 2 and args[0] == "user":
    for i in wtmp_read():
      if args[1] in i:
        print i

#################################################
#             reading secure log
#################################################
def list_secure_log():
  # Path to secure file
  secure_path = "/var/log/secure"
  # Read content of secure file
  try:
    rfile = open(secure_path, "r")
    lines = rfile.readlines()
    rfile.close()
  except IOError:
    sys.exit("Could not read file - Are you root?")
  # Save only lines relevant to sudo use
  sudo_lines = []
  for i in lines:
    if "sudo" in i:
      sudo_lines.append(i[:-1])
  # Print all the sudo lines
  for i in sudo_lines:
    print i

#################################################
#             reading firefox urls
#################################################
def firefox_url_history():
    """sqlite3 query based off of query from www.alekz.net/archives/740"""
    db_query = ("SELECT datetime(moz_historyvisits.visit_date/1000000,\"unixepoch\"), moz_places.url "
                "FROM moz_places, moz_historyvisits "
                "WHERE moz_places.id = moz_historyvisits.place_id")

    conn = sqlite3.connect('/home/voot/.mozilla/firefox/swpficl5.default/places.sqlite')
    hist_cursor = conn.cursor()

    for row in hist_cursor.execute(db_query):
        print row
    conn.close()  


#################################################
#            reading MySQL logs 
#################################################

#################################################
#            print out the usage 
#################################################
def usage():
    print "Usage: %s {wtmp|priv_esc|firefox|mysql}" % sys.argv[0]
    sys.exit(1)

if __name__ == '__main__':
  if len(sys.argv) == 1:
    usage()
  if sys.argv[1] == "wtmp":
    wtmp_parse(sys.argv[2:])
  elif sys.argv[1] == "priv_esc":
    list_secure_log()
  elif sys.argv[1] == "firefox":
    firefox_url_history()
  elif sys.argv[1] == "mysql":
    pass
  else:
    usage()
