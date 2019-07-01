import socket
import sys
from AutomateRecording import AutomateRecording
 
# argv 1 : automate id
# argv 2 : automate port

if not (len(sys.argv) >= 3):
    print("Need to give automate ID and PORT as ARGV!")
else:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('', int(sys.argv[2])))
    serverSocket.listen(5)
    runServer = True
    if len(sys.argv) == 4:
        haveError = True
    print("Start automate " + sys.argv[1] + " at " + sys.argv[2])
    while runServer:
        clientSocket, clientInfo = serverSocket.accept()
        automate = AutomateRecording(int(sys.argv[1]), haveError)
        clientSocket.send(str.encode(automate.toJSON()))
        clientSocket.close()
    serverSocket.close()