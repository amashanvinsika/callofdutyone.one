# Auto rotating console messages 
# For Call of Duty v1.1
#A m a s h a n#

import socket
import time
 
host = "225.225.225.225" #your servers ip
port = 28960 #your servers port
rcon_password = "rconpass" #your servers rcon password
command = "say" #command
interval = 1 #in minutes
messages = [ 'message1', 'message2', 'message3', 'message4'] #message list

 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect((host, port))
i = 0
while True:
   print("Sending..")
   sock.send("\xFF\xFF\xFF\xFFrcon %s %s %s\0" % (rcon_password, command, messages[i%len(messages)]));
   i=i+1
   time.sleep(60*interval) 
