# lab-resource
Basically speaking, this is to help us with monitoring computers and devices in the lab.

Current functionality:
  A. Present a simple website
  B. SQLite database to store data (may move to MySQL cluster later)
  C. A basic socket server with a basic socket client to submit data

This is a program combining of:
  A. socket server
  B. web server
  C. other necessary library for adb, sql, and so on.
  D. client to sent message to server

1. installation of tornado webserver is required
2. just do "python labmonitor.py", and set crontab for clients to run "python client.py"
   ...everything is done
