# from wsgiref.simple_server import make_server
#
# from webtest import application
#
# httpd = make_server('', 8000, application)
# print('Serving HTTP on port 8000')
# httpd.serve_forever()

import socket

def service_client(new_socket):
    # 1.接收浏览器发送过来的请求，即http请求
    # GET / HTTP/1.1
    request = new_socket.recv(1024)
    print(request)
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"
    response += "<h1>hahaha</h1>"
    new_socket.send(bytes(response,encoding='utf-8'))
    new_socket.close()

def main():
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定端口
    tcp_server_socket.bind(("", 7890))
    # 3.变为监听套接字
    tcp_server_socket.listen(128)
    # 4.等待新客户端的链接
    new_socket, client_addr = tcp_server_socket.accept()
    # 5.为这个客户端服务
    service_client(new_socket)


if __name__ == "__main__":
    main()