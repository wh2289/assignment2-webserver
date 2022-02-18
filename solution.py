from socket import *
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", port))
    serverSocket.listen(1)
    print('Waiting for connection')
    while True:
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        try:

            try:
                message =  connectionSocket.recv(1024)
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata =  f.read()
                print(outputdata)


                connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())

                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())

                connectionSocket.send("\r\n".encode())
                connectionSocket.close()
            except IOError:

                connectionSocket.send('HTTP/1.1 400 Not Found'.encode())

                connectionSocket.close()


        except (ConnectionResetError, BrokenPipeError):
            pass

    serverSocket.close()
    sys.exit()


if __name__ == "__main__":
    webServer(13331)