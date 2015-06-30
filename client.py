import os
import re
import socket
import sys
from utilities.adb_helper import AdbHelper

control_server_ip = "localhost"
control_server_port = 10054

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (control_server_ip, control_server_port)
print 'Connecting to %s:%s' % server_address
sock.connect(server_address)

data = sock.recv(1024).strip()
if data <> "<< Control Server Connected >>":
    print "Successfully connected to the control server.\n"
    sys.exit()

try:
    # Send data
    adb_devices = AdbHelper.adb_devices()
    for device in adb_devices.items():
        message = ""

        # Check for device type
        if device[1] == "device":
            device_type = re.sub(r'\r+|\n+', '', AdbHelper.adb_shell('getprop ro.product.device', serial=device[0]))
        else:
            device_type = "unknown"

        # Check for device build
        if device[1] == "device":
            device_build = re.sub(r'\r+|\n+', '', AdbHelper.adb_shell('getprop ro.build.version.incremental', serial=device[0]))
        else:
            device_build = "unknown"

        # Check for device status
        if device[1] == "device":
            if os.path.isfile("/tmp/LOCKS/" + device[0] + ".lock"):
                device_avail = "locked"
            else:
                device_avial = "available"
        else:
            device_avial = "unavailable"

        message += "{\"ident\":\"info\","
        message +=  "\"serial\":\"" + device[0] + "\","
        message +=  "\"status\":\"" + device[1] + "\","
        message +=  "\"type\":\"" + device_type + "\","
        message +=  "\"availability\":\"" + device_avial + "\","
        message +=  "\"build\":\"" + device_build + "\""
        message += "}"

        print 'Sending %s' % message
        sock.sendall(message)

        # Look for the response
        data = sock.recv(1024).strip()
        print 'Received %s' % data

finally:
    print 'Closing socket'
    sock.close()
