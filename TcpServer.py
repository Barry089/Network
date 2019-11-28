import socket
from time import ctime


HOST = 'localhost'
PORT = 5008
BUF_SIZE = 1024
ADDRESS = (HOST, PORT)

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(ADDRESS)
    server_socket.listen(5)
    print("正在监听：%s : %d" % (HOST, PORT))

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    while True:
        print(u'服务器等待连接.....')
        client_socket, address = server_socket.accept()
        print(u'连接客户端地址：', address)

        while True:
            data = client_socket.recv(BUF_SIZE)
            print('来自客户端的消息：%s' % data.decode('utf-8'))
            print('发送服务器时间给客户端：%s' % ctime())

            try:
                client_socket.send(bytes(ctime(), 'utf-8'))
            except KeyboardInterrupt:
                print("用户取消")

        client_socket.close()

        server_socket.close()
