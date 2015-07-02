#!/usr/bin/python

import server
import webserver
import subprocess
import time

class CmdProcessor():
    _INPUT_EXIT_COMMAND = 'exit'
    _INPUT_NONE = ''

    def __init__(self, **kwargs):
        self.ss = subprocess.Popen(["python", "server.py"])
        self.ws = subprocess.Popen(["python", "webserver.py"])
        time.sleep(2)
        self.cmd()

    def cmd(self):
        print 'Enter \'%s\' or Crtl+D to exit the shell.' % self._INPUT_EXIT_COMMAND
        print 'And enter \'help\' for more commands.'
        try:
            while True:
                input = raw_input(">> ")
                # if input is EXIT command, exit this program
                if input.lower() == self._INPUT_EXIT_COMMAND:
                    break

                # if input is NONE, then do nothing and keep going...
                elif input.strip() == self._INPUT_NONE:
                    continue

                # execute the command.
                else:
                    self.command(input)

        except Exception as e:
            print e

        self.goodbye()        
        exit()

    def command(self, input):
        print input + " received."

    def goodbye(self):
        print "Good Bye!"
        self.ss.kill()
        self.ws.kill()

def main():
    CmdProcessor()

if __name__ == "__main__":
    main()
