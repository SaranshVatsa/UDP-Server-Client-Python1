import socket
serverName=''  #Enter IP of the Server here between the inverted commas.
serverPort=12000   #Port number can be changed.
clientSocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message=input('Input lowercase: ')
clientSocket.sendto(message.encode('utf-8'),(serverName,serverPort))
modifiedMessage, returnAddress= clientSocket.recvfrom(2048)
print (modifiedMessage.decode('utf-8'))
clientSocket.close()

