from socket import *
serverPort = 13331
def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  serverSocket.bind(("", port))
  serverSocket.listen(1)
  #Fill in start
  print('The server is up on port 1331', serverPort)
  #Fill in end

  while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = #Fill in start      #Fill in end
    try:

      try:
        message = #Fill in start    #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = #Fill in start     #Fill in end
        
        #Send one HTTP header line into socket.
        #Fill in start

        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
      except IOError:
        # Send response message for file not found (404)
        #Fill in start
    print('404 Not Found')
        #Fill in end


        #Close client socket
        #Fill in start

        #Fill in end

    except (ConnectionResetError, BrokenPipeError):
      pass

  serverSocket.close()
  sys.exit()

if __name__ == "__main__":
  webServer(13331)