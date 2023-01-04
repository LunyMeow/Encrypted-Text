import socket
import threading
import sys
import Ceasar

#Wait for incoming data from server
#.decode is used to turn the message in bytes to a string
password=input("Password: ")
def receive(socket, signal):
    while signal:
        try:
            data = socket.recv(32)
            data=Ceasar.decrypt(password,data.decode("utf-8"))
            print(str(data))
        except Exception as e:
            print(e)
            print("You have been disconnected from the server")
            signal = False
            break

#Get host and port
host = input("Host: ")
port = int(input("Port: "))

#Attempt connection to server
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    
except:
    print("Could not make a connection to the server")
    input("Press enter to quit")
    sys.exit(0)

#Create new thread to wait for data
receiveThread = threading.Thread(target = receive, args = (sock, True))
receiveThread.start()

#Send data to server
#str.encode is used to turn the string message into bytes so it can be sent across the network

#sock.sendall(Ceasar.encrypt(password,str.encode(f"passwordis:{password}")))
sock.sendall(str.encode(Ceasar.encrypt(password,f"passwordis{password}")))
while True:
    message = input()
    message=Ceasar.encrypt(password,message)
    sock.sendall(str.encode(message))
