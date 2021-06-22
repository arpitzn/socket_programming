import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#now what is my receiver address

recv_addr = ("127.0.0.1",9000)
while 2>1:
    # now i want to send message 
    user_data = input("enter your message here")

    #converting data into ascii
    new_data = user_data.encode('ascii')

    #now you can send message 
    s.sendto(new_data, recv_addr)

    print("your message is sent")

# import socket 
# import time
# # import socket module /library to create 
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# # what is my receiver address
# recv_addr=("127.0.0.1",9999)
# # Now i want to send message
# while 2 > 1 :
#     user_data=input("enter your message :- ")
#     # converting data into ascii code
#     newdata=user_data.encode('ascii')
#     # now you can send data 
#     s.sendto(newdata, recv_addr)
#     time.sleep(2)
#     print("your message has been sent..")
#     # now waiting for reply 
#     print(s.recvfrom(10))