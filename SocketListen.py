#import socket module 
from socket import *          
serverSocket = socket(AF_INET, SOCK_STREAM) #Create the Socket Object
#Prepare a sever socket 
#Fill in start 
port = 8000 #port number
serverSocket.bind(('0.0.0.0',port)) #binds the server to localhost by default
serverSocket.listen(1) #listens to program

print "THE Server is READY! AYE AYE CAPTAIN"
print serverSocket

while True: 
    #Establish the connection 
    print 'Ready to server...' 
    connectionSocket, addr = serverSocket.accept() #Fill in start             #Fill in end 
    try: 
        message = connectionSocket.recv(1024) #You get the raw object
        #INSERT PARSING#
        #Fill in end         
        
        #Send the content of the requested file to the client        
        connectionSocket.send(outputdata) #If you wanna send data back
        connectionSocket.close() #Closing the connection to the client if you want
        print "File receieved"  
serverSocket.close()
