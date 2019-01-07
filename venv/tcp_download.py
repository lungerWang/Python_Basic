import socket

def main():
    tcp_socket = socket.socket(socket.AF_ASH, socket.SOCK_STREAM)
    dest_ip = input("请输入目标ip")
    dest_port = input("请输入目标端口")
    tcp_socket.connect((dest_ip, dest_port))
    download_name = input("请输入要下载的文件名")
    tcp_socket.send(download_name.encode("utf-8"))

    recv_data = tcp_socket.recv(1024)
    with open(download_name, "wb") as f:
        f.write(recv_data)

    tcp_socket.close()

if __name__ == "__main__":
    main()