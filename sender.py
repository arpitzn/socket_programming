import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#now what is my receiver address

recv_addr = ("127.0.0.1", 9999)

# now i want to send message 
user_data = input("enter your message here")

#converting data into ascii
new_data = user_data.encode('ascii')

#now you can send message 
s.sendto(new_data, recv_addr)

print("your message is sent")