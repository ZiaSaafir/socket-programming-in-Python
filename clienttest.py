import socket

# Create a TCP socket
ob = socket.socket()

# Connect to the server
# localhost = same computer
# 2301 = server's port
ob.connect(('localhost', 2301))

# Create a message
# msg = 'hello this is first client'

# ob.send(msg.encode('utf-8'))

conn=True
while conn:
    msg=input("Enter message to send to server: ")
    ob.send(msg.encode('utf-8'))
    if msg=='no':
        conn=False
        ob.close()

