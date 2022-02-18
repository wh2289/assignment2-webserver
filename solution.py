from socket import *
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", port))
    serverSocket.listen(1)
    print('Waiting for connection')
    while True:
        # Establish the connection
        # print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        try:

            try:
                message =  connectionSocket.recv(1024)
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata =  f.read()

                # Send one HTTP header line into socket.
                # Fill in start

                # Fill in end

                # Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())

                connectionSocket.send("\r\n".encode())
                connectionSocket.close()
            except IOError:
        # Send response message for file not found (404)
        # Fill in start

        # Fill in end

        # Close client socket
        # Fill in start

        # Fill in end

        except (ConnectionResetError, BrokenPipeError):
            pass

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)