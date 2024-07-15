import socket 
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM )   # UDP 

target_ip = "192.168.1.72" 
# target_ip = "127.0.0.1" 
port_no = 2525 
target_address = (target_ip,port_no)

condition = True
while condition:
    message = input("Plz write your message here : ")
    encrypt_message = message.encode('ascii')
    s.sendto(encrypt_message,target_address)