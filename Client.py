from socket import *
import threading, os, sys


def recvmsg():
    while 1:
        try:
            receivedMsg = clientSocket.recv(2048)
            if receivedMsg.decode() != '':
                print(receivedMsg.decode())
        except ConnectionResetError:
            clientSocket.close()
            break
    os._exit(0)


def sendmsg():
    while 1:
        try:
            yourSentMsg = input("")
            if yourSentMsg != 'exit()':
                clientSocket.send(yourSentMsg.encode())
            else:
                clientSocket.close()
                break
        except ConnectionResetError:
            clientSocket.close()
            break
    os._exit(0)

def StartClient(ip,port):
    if not ip:
        ip = 'localhost'
    if not port:
        port = 9999   
    clientSocket.connect((ip, int(port)))
    #print("The Client is READY to RECEIVE via TCP @", serverPort)
    #print(clientSocket)
    threads = [threading.Thread(target=recvmsg), threading.Thread(target=sendmsg)]
    for t in threads:
        t.start()

if __name__ == '__main__':
    clientSocket = socket(AF_INET, SOCK_STREAM)
    TargetIP = input("Please enter server IP: ")
    TargetPort = input("Please enter server Port: ")
    StartClient(TargetIP,TargetPort)
