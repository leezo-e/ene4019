
from socket import *

serverName = '127.0.0.1'

serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM) #소켓 생성hi

clientSocket.connect((serverName, serverPort)) #서버 

sentence = input('Input lowercase sentence')

clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(1024)

print('From Server: ', modifiedSentence.decode())

clientSocket.close()

 