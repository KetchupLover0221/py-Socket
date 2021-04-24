from socket import *
import threading, time, os, sys, getopt

def Recvmsg():
        while 1:
            try:
                recvmsg, fromadd = client.recvfrom(2048)
                print(fromadd[1], ': ', recvmsg.decode())
            except ConnectionResetError:
                client.close()
                break

def Sendmsg(port):
    while 1:
        send = input()
        client.sendto(send.encode(),('localhost',int(port)))
        if send == 'exit()':
            client.close()
            break

def start(port1,port2):
    ip = 'localhost'
    client.bind((ip, int(port1)))
    threads = [threading.Thread(target=Sendmsg, args=(port2,)), threading.Thread(target=Recvmsg)]
    for t in threads:
        t.start()

if __name__ == "__main__":
    client = socket(AF_INET, SOCK_DGRAM)
    port1 = input("Type your port: ")
    port2 = input("Type target port: ")
    start(port1,port2)