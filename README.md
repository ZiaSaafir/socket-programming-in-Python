# Socket Programming in Python

A beginner-friendly project to understand **socket programming in Python** through practical client-server examples using **TCP and UDP**.

This project explains how two programs can communicate with each other over a network using Python's built-in `socket` module.

## What You Will Learn

* What socket programming is
* Client and server communication
* IP addresses and ports
* `localhost`
* TCP socket programming
* UDP socket programming
* Creating a server
* Creating a client
* `bind()`
* `listen()`
* `accept()`
* `connect()`
* `send()` and `sendto()`
* `recv()` and `recvfrom()`
* Encoding and decoding messages
* Handling multiple messages with loops

## Project Structure

```text
socket-programming-python/
│
├── tcp_server.py
├── tcp_client.py
├── udp_server.py
├── udp_client.py
└── README.md
```

## Requirements

You only need:

* Python 3.x
* A code editor such as VS Code
* Basic Python knowledge

No external Python libraries are required.

## TCP Communication

TCP provides a **reliable and connection-oriented** way for the client and server to communicate.

### TCP Server

The server:

1. Creates a socket
2. Binds to an IP address and port
3. Starts listening
4. Accepts a client connection
5. Receives messages
6. Processes the messages
7. Closes the connection

### TCP Client

The client:

1. Creates a socket
2. Connects to the server
3. Sends messages
4. Closes the connection

### Run TCP Example

First start the server:

```bash
python tcp_server.py
```

Then open another terminal and run:

```bash
python tcp_client.py
```

The basic communication flow is:

```text
Client
   |
   | connect()
   ↓
Server
   |
   | accept()
   ↓
Connection Established
   |
   | send()
   ↓
Server
   |
   | recv()
   ↓
Message Received
```

## UDP Communication

UDP is a **connectionless** communication protocol.

Unlike TCP, UDP does not establish a connection before sending data.

The sender directly sends a datagram to the receiver's IP address and port.

### UDP Server

The UDP server:

1. Creates a UDP socket
2. Binds to an IP address and port
3. Waits for datagrams
4. Receives messages using `recvfrom()`
5. Sends responses using `sendto()`

### UDP Client

The UDP client:

1. Creates a UDP socket
2. Creates a message
3. Sends it using `sendto()`
4. Receives a response using `recvfrom()`

### Run UDP Example

First start:

```bash
python udp_server.py
```

Then run:

```bash
python udp_client.py
```

## TCP vs UDP

| Feature       | TCP                             | UDP                      |
| ------------- | ------------------------------- | ------------------------ |
| Connection    | Connection-oriented             | Connectionless           |
| Reliability   | Reliable                        | Not guaranteed           |
| Ordering      | In-order                        | Not guaranteed           |
| Speed         | Generally slower                | Generally faster         |
| Communication | `connect()`, `send()`, `recv()` | `sendto()`, `recvfrom()` |
| Common Use    | Web, file transfer, email       | Streaming, gaming, DNS   |

## Important Socket Functions

| Function     | Purpose                                |
| ------------ | -------------------------------------- |
| `socket()`   | Creates a socket                       |
| `bind()`     | Assigns IP and port to a server        |
| `listen()`   | Makes TCP server ready for connections |
| `accept()`   | Accepts a TCP client                   |
| `connect()`  | Connects TCP client to server          |
| `send()`     | Sends TCP data                         |
| `recv()`     | Receives TCP data                      |
| `sendto()`   | Sends UDP data                         |
| `recvfrom()` | Receives UDP data                      |
| `close()`    | Closes a socket                        |

## Important Concept

In TCP server programming, there are usually two important sockets:

```text
ob
│
└── Listening socket
    Waits for clients

clientobject
│
└── Communication socket
    Communicates with the connected client
```

The `accept()` function creates the communication socket for a connected client:

```python
clientobject, add = ob.accept()
```

Here:

* `clientobject` → socket used for communication
* `add` → client's address

## Learning Goal

The main goal of this project is not just to memorize socket functions.

It is to understand the complete communication process:

```text
Application
     ↓
Socket
     ↓
TCP / UDP
     ↓
Network
     ↓
Other Computer
     ↓
Socket
     ↓
Application
```

## Practice Ideas

After understanding the examples, try to build:

1. A client that sends user input
2. A server that replies to the client
3. A multi-message chat
4. A simple two-way chat application
5. A server that handles multiple clients
6. A simple file-transfer application

## Author

**Ziaullah**

Learning Python, Computer Networking, and Backend Development.

---

## License

This project is created for **learning and educational purposes**.
