import socket
serverPort=12000
serverSocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((' ', 12000))
print("The server is ready to use. Using UDP.")
while 1:
    message, clientAddress=serverSocket.recvfrom(2048)
    decmes=message.decode('utf-8')
    print("Message received.")
    modifiedMes=decmes.upper()
    serverSocket.sendto(modifiedMes.encode('utf-8'), clientAddress)
