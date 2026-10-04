import socket

# Create TCP socket
ob = socket.socket()

# Bind server to localhost and port 2301
ob.bind(('192.168.1.17', 2301))

# Start listening for clients
ob.listen(4)

# Server is ready
print("Server is ready to accept connection")

# Accept client connection
clientobject, add = ob.accept()

# Display client address
print("Connected with this address:", add)

conn = True

while conn:

    # Receive maximum 1024 bytes
    gotmsg = clientobject.recv(1024)

    # Convert bytes into string
    gotmsg = gotmsg.decode('utf-8')

    # Display received message
    print("Received message:", gotmsg)

    # Stop if client sends empty message or 'no'
    if len(gotmsg) == 0 or gotmsg == 'no':
        conn = False

# Close client socket
clientobject.close()

# Close server socket
ob.close()