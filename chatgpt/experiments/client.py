#! /usr/bin/python2
# -*- encoding: UTF-8 -*-



# import socket

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect(('localhost', 8080))
#     s.sendall(b'Hello, world')
#     data = s.recv(1024)

# print('Received', repr(data))

# print("Testing subprocess")

# import json
# import zmq

# # Create a ZeroMQ context
# context = zmq.Context()

# # Create a ZeroMQ socket of type REP (reply)
# socket = context.socket(zmq.REP)

# # Bind the socket to a port
# socket.bind("tcp://*:5555")

# # Wait for incoming messages
# while True:
#     message = socket.recv()
#     print("Received message: %s" % message)

#     # Parse the message as a JSON object
#     data = json.loads(message)

#     # Process the data
#     result = {"sum": sum(data)}

#     # Serialize the result as a JSON object
#     response = json.dumps(result)

#     # Send the response back to the sender
#     socket.send(response)



# import json
# import socket

# # Create a socket and bind it to a port
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind(('localhost', 8000))
# sock.listen(1)

# # Wait for a client to connect
# print("Waiting for client...")
# conn, addr = sock.accept()
# print("Client connected:", addr)

# # Receive JSON data from the client
# data = conn.recv(1024)
# json_data = json.loads(data)
# print("Received data:", json_data)

# # Send JSON data back to the client
# json_data['response'] = "Hello from Python 2.7"
# conn.send(json.dumps(json_data))

# # Close the connection
# conn.close()

import naoqi


print("bara choda")