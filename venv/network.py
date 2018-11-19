# Socket是网络编程的一个抽象概念。通常我们用一个Socket表示打开了一个网络连接，而打开一个Socket需要知道目标ip地址、端口号及连接协议
# 建立tcp连接时，主动发起的一方叫做客户端，被动连接的一方叫服务器
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn', 80))
# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)
s.close()
print(data)
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('sina.html', 'wb') as f:
    f.write(html)