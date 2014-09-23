#!/usr/bin/python

import sys
import os

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


if __name__ == '__main__':
  if sys.argv[1] == "wtmp":
    wtmp_parse(sys.argv[2:])
  elif sys.argv[1] == "priv_esc":
    list_secure_log()
  elif sys.argv[1] == "firefox":
    pass
  elif sys.argv[1] == "mysql":
    pass
  else:
   print "Usage: %s {wtmp|priv_esc|firefox|mysql}" % sys.argv[0]

