from socket import *
import threading, time


def intermsg(users, client, username):
    print('User Port: ' + str(client[1]))
    while 1:
        try:
            receivedMsg = users[client].recv(40960)
            now = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
            if receivedMsg.decode() != '':
                print(now + " The Server has received '" + receivedMsg.decode() + "' from " + str(client[1]) )
                #服务端收到来自用户的消息

                recvSentMsg = '\n'+ now + ' ' + username +': ' + '\n' + receivedMsg.decode()+'\n'
                for u in users.values():
                    u.send(recvSentMsg.encode())
                #所有用户都收到消息

        except ConnectionResetError:
            print(str(client[1]) + ' has exited.')
            break



def close():
    while 1:
        cmd = input()
        if cmd == 'exit()':
            for u in users.values():
                u.close()
            break
    os._exit(0)#服务端关闭


def login(clientsocket, client):
    while 1:
        usrAsk = 'Enter your username: '
        clientsocket.send(usrAsk.encode())
        usrAns = clientsocket.recv(2048)
        print(usrAns.decode())
        #用户名
        pwdAsk = 'Enter your password: '
        clientsocket.send(pwdAsk.encode())
        pwdAns = clientsocket.recv(2048)
        print(pwdAns.decode())
        #密码
        usrpwd = [usrAns.decode(), pwdAns.decode()]
        #对比主函数中的用户列表判断该用户是否合法
        if usrpwd in admin:
            success = usrpwd[0] + ' Login Success!'
            clientsocket.send(success.encode())
            time.sleep(1)
            users[client] = clientsocket
            print(usrpwd[0], ' has connected.')
            break

        else:
            failed = 'Login Failed!'
            clientsocket.send(failed.encode())
            time.sleep(1)

    threading.Thread(target=intermsg, args=(users, client, usrAns.decode())).start()
    #支持多线程同时登陆

def StartServer(ip,port):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((ip, port))
    serverSocket.listen(50)
    print("The Server is READY to RECEIVE via TCP @", port)
    threading.Thread(target=close).start()
    while 1:
        connectionSocket, clientAddr = serverSocket.accept()
        print(connectionSocket)
        #打印服务端连接信息
        threading.Thread(target=login, args=(connectionSocket, clientAddr)).start()


if __name__ == '__main__':
    admin = [['tyz', '123'],['abc','456']]
    users = {}
    StartServer('localhost',9999)
    os._exit(0)