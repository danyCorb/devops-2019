import socket
import json 
from AutomateRecording import AutomateRecording

automate = AutomateRecording(1)


print(json.dumps(props(automate)))

# serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# serverSocket.bind(('', 8002))
# serverSocket.listen(5)

# runServer = true

# while runServer:
#     clientSocket, clientInfo = serverSocket.accept()
#     clientSocket.send(b"Je viens d'accepter la connexion")
#     clientSocket.close()

# serverSocket.close()