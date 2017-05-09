#!/usr/bin/env python
import sys
import argparse

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def processCmdLineOptions():
  global optparser
  optparser = argparse.ArgumentParser(description="ftpserver-cli",
              formatter_class=argparse.RawDescriptionHelpFormatter)
  optparser.add_argument('-u', '--username', action='store', type=str,
      default="user", help="username")
  optparser.add_argument('-p', '--password', action='store', type=str,
      default="12345", help="password")
  optparser.add_argument('-t', '--port', action='store', type=int,
      default="21", help="port")
  optparser.add_argument('-d', '--directory', action='store', type=str,
      default="/", help="port")
  optargs = optparser.parse_args(sys.argv[1:]) #(sys.argv)
  return optargs


# -------------------------------------
def main(argv):
# -------------------------------------
  try:
    if len(argv) == 0:
      
      print "\nUsage: # python ftpserver.py [-h] [-u USERNAME] [-p PASSWORD] [-t PORT] [-d DIRECTORY]\n"
      exit(1)

    else:
      optargs = processCmdLineOptions()

      print("Using: user: %s pass: %s port: %d dir: %s" % (optargs.username, optargs.password, optargs.port, optargs.directory))

      authorizer = DummyAuthorizer()
      authorizer.add_user(optargs.username, optargs.password, optargs.directory, perm="elradfmw")

      handler = FTPHandler
      handler.authorizer = authorizer

      server = FTPServer(("127.0.0.1", optargs.port), handler)
      server.serve_forever()

  except KeyboardInterrupt:
    print " Identified. Program Terminated"
  except Exception as Ae:
    print "Program Terminated" + str(Ae)


# -------------------------------------
if __name__ == '__main__':
# -------------------------------------
  main(sys.argv[1:])


