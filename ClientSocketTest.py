from socket import *
import socket
import base64
import ssl
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "smtp.gmail.com"
#Fill in start #Fill in end
port = 587
recipient = "<nzDSKE@gmail.com>"
sender = "<nzDSKE@gmail.com>"
username = "nzDSKE"
password = 'abcd1234567890abcd'
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket.socket()
clientSocket.connect((mailserver,port))
#Fill in end
recv = clientSocket.recv(1024)
print "="*21
print recv
if recv[:3] != '220':
	print '220 reply not received from server.'
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'
print "="*21

#Log_In SSL 
clientSocket.send('STARTTLS\r\n')
tls_recv = clientSocket.recv(1024)
print tls_recv
if tls_recv[:3] != '220':
	print '220 reply not received from server'

#SSL optional
ssl_cs = socket.ssl(clientSocket)
ssl_cs.write('AUTH LOGIN\r\n')
auth_recv = ssl_cs.read(1024)
print auth_recv, "auth"
if auth_recv[:3] != '334':
	print '334 reply not received from server'
username = base64.b64encode(username) + '\r\n'
ssl_cs.write(username)
username_recv = ssl_cs.read(1024)
print username_recv
if username_recv[:3] != '334':
	print '334 reply not received from server'
password = base64.b64encode(password) + '\r\n'
ssl_cs.write(password)
password_recv = ssl_cs.read(1024)
print password_recv
if password_recv[:3] != '235':
	print '235 reply not received from server'

print "="*21

# Send MAIL FROM command and print server response.
# Fill in start
print "="*21
mailFromCommand = 'MAIL FROM: ' + sender + '\r\n'
ssl_cs.write(mailFromCommand)
recv2 = ssl_cs.read(1024)
print recv2
if recv2[:3] != '250':
	print '250 reply not received from server.'
print "="*21
# Fill in end
# Send RCPT TO command and print server response.
# Fill in start
print "="*21
rcptToCommand = 'RCPT TO: ' + recipient + '\r\n'
ssl_cs.write(rcptToCommand)
recv3 = ssl_cs.read(1024)
print recv3
if recv3[:3] != '250':
	print '250 reply not received from server.'
print "="*21
# Fill in end
# Send DATA command and print server response.
# Fill in start
print "="*21
ssl_cs.write('DATA\r\n')
recv4 = ssl_cs.read(1024)
print recv4
if recv4[:3] != '354':
	print '354 reply not received from server.'
print "="*21
# Fill in end
# Send message data.
# Fill in start
ssl_cs.write(msg)
# Fill in end
# Message ends with a single period.
# Fill in start
ssl_cs.write(endmsg)
recv5 = ssl_cs.read(1024)
print recv5
if recv5[:3] != '250':
	print '250 reply not received from server.'
# Fill in end
# Send QUIT command and get server response.
# Fill in start
ssl_cs.write('QUIT\r\n')
recv6 = ssl_cs.read(1024)
print recv6
if recv6[:3] != '221':
	print '221 reply not received from server.'

clientSocket.close()
# Fill in end