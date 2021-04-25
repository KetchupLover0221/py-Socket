# py-Socket
2020-2021 学年春季学期《计算机网络》Socket 实验

## 程序文件列表

```shell
py-socket
|
├───README.md
│
├───TCP	// 基于TCP协议
│       client.py		// 客户端
│       server.py		// 服务端
│
└───UDP	// 基于UDP协议
       client.py  		// 客户端/服务端
```

## 环境

1. 程序整体在 ```Python3.9.0``` 下实现

2. 基于 ```Socket ```库实现局域网通讯功能

3. 基于 ```threading``` 库实现多线程的收发消息功能

4. 基于```time``` 库显示时间

## 使用

克隆项目

```bash
git clone git@github.com:KetchupLover0221/py-Socket.git
```

### 1）UDP 程序


打开两个命令行或Shell，运行client客户端

```shell
python Client.py
```

根据提示在两个命令行窗口中输入自己的端口与对方的端口以完成连接

输入发送内容，按 ```Enter``` 以发送

任意一方发送  `exit()`断开连接

### 2）TCP 程序

#### 服务端

打开命令行或Shell，输入：

```shell
python Server.py
```
显示：`The Server is READY to RECEIVE via TCP @ 9999`

表明服务端已正常打开，端口：`9999` 正在等待客户连接


#### 客户端
打开一个或多个命令行或 Shell，输入:

```shell
python Client.py
```

根据程序提示，输入服务端 IP 地址与端口

如：

```
Please enter server IP: localhost
Please enter server Port: 9999
```

默认为 ```'localhost', 9999```

若连接成功，此时服务端显示：

```
<socket.socket fd=644, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9999), raddr=('127.0.0.1', 51237)>
```
根据程序提示，输入用户名与密码以登录

```
	测试用户名：tyz
	测试密码：123
```

若登录成功，此时服务端显示：

```
tyz  has connected.
User Port: 51237
```

客户端显示：

```
tyz Login Success!
```

否则，客户端显示：

```
Login failed!
```



#### 通讯过程

在任一客户端中输入发送内容，按```Enter```以发送

若发送成功，此时服务端显示：

```
2021/04/25 14:36:21 The Server has received '你好' from 51237
```

各客户端显示：

```
2021/04/25 14:36:21 tyz:
你好
```

在任一客户端中输入 ```exit()``` 以退出登录

此时服务端显示：

```
51237 has exited.
```

