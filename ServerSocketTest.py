#import socket module 
from socket import *                                   
serverSocket = socket(AF_INET, SOCK_STREAM) 
#Prepare a sever socket 
#Fill in start 
port = 8000 #port number
serverSocket.bind(('0.0.0.0',port)) #binds the server to localhost by default
serverSocket.listen(1) #listens to program
print "THE Server is READY! AYE AYE CAPTAIN"
print serverSocket
#Fill in end 
while True: 
    #Establish the connection 
    print 'Ready to server...' 
    connectionSocket, addr = serverSocket.accept() #Fill in start             #Fill in end 
    try: 
        message = connectionSocket.recv(1024) #Fill in start          #Fill in end
        print message,'\n'
        filename = message.split()[1]                  
        f = open(filename[1:])                         
        outputdata = f.read()#Fill in start       #Fill in end
        #Send one HTTP header line into socket 
        #Fill in start 
        connectionSocket.send("\n HTTP/1.1 200 OK \n")
        #Fill in end                 
        #Send the content of the requested file to the client 
        for i in range(0, len(outputdata)):            
            connectionSocket.send(outputdata[i]) 
        connectionSocket.close()
        print "File receieved"
    except IOError:
        #Send response message for file not found 
        #Fill in start
        connectionSocket.send("\n 404 Not Found \n")
        #Fill in end 
        #Close client socket
        #Fill in start 
        connectionSocket.close()
        #Fill in end        
serverSocket.close()
