#server
import socket

s = socket.socket()
port = 12121
# sendData="content not found"
s.bind(('', port))
# filecontent={"20bcs001","20bcs002","20bcs003"}
s.listen(5)
c, addr = s.accept()
print ("Socket Up and running with a connection from",addr)
while True:
    rcvdData = c.recv(1024).decode()
    print ("request from clint:",rcvdData)
    # if(rcvdData=="Aakash"):
    #    c.send(filecontent[0])
    # elif(rcvdData=="dubay"):
    #     c.send(filecontent[1].encode())
    # else:
    #     c.send(sendData.endcode())      
    sendData = input("N: ")
    c.send(sendData.encode())
    if(rcvdData == "Bye" or rcvdData == "bye"):
        break
c.close()

########################################clint
import socket

s = socket.socket()
s.connect(('127.0.0.1',12121))
while True:
    str = input("clint_message: ")
    s.send(str.encode())
    if(str == "Bye" or str == "bye"):
        break
    print ("Responce from server:",s.recv(1024).decode())
s.close()

