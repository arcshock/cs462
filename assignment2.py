#!/usr/bin/python

import struct
import sys
import pwd
import time
import sqlite3

################################################
#           user logins
################################################
def getrecord(file,uid, preserve = False):
  """Returns [int(unix_time),string(device),string(host)] from the lastlog formated file object, set preserve = True to preserve your position within the file"""
  position = file.tell()
  recordsize = struct.calcsize('L32s256s')
  file.seek(recordsize*uid)
  data = file.read(recordsize)
  if preserve:
    file.seek(position)
  try:
    returnlist =  list(struct.unpack('L32s256s',data))
    returnlist[1] = returnlist[1].replace('\x00','')
    returnlist[2] = returnlist[2].replace('\x00','')
    return returnlist
  except:
    return False

def list_wtmp():
  try:
    llfile = open("/var/log/lastlog",'r')
  except:
    print "Unable to open /var/log/lastlog"
    sys.exit(1)

  for user in pwd.getpwall():
    record = getrecord(llfile,user[2])
    if record and record[0] > 0:
      #print '%16s\t\t%s\t%s' % (user[0],time.ctime(record[0]),record[2])
      print user[0],record[0],record[2]
    elif record:
      print '%16s\t\tNever logged in' % (user[0],)
    else:
      pass
  llfile.close()

#################################################
#             reading secure log
#################################################
def list_secure_log():
  secure_path = "/var/log/secure"
  rfile = open(secure_path, "r")
  lines = rfile.readlines()
  rfile.close()
  sudo_lines = []
  for i in lines:
    if "sudo" in i:
      sudo_lines.append(i[:-1])

  for i in sudo_lines:
    print i

#################################################
#             reading firefox urls
#################################################
def firefox_url_history():
    conn = sqlite3.connect('/home/voot/.mozilla/firefox/swpficl5.default/places.sqlite')
    hist_cursor = conn.cursor()

    for row in hist_cursor.execute('SELECT datetime(moz_historyvisits.visit_date/1000000,"unixepoch"), moz_places.url FROM moz_places, moz_historyvisits WHERE moz_places.id = moz_historyvisits.place_id'):
        print row
    conn.close()  


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
    list_wtmp()
  elif sys.argv[1] == "priv_esc":
    list_secure_log()
  elif sys.argv[1] == "firefox":
    firefox_url_history()
  elif sys.argv[1] == "mysql":
    pass
  else:
    usage()
