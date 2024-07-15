import socket 
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM )   # UDP 
ip_address = "192.168.1.72"   # available 
# ip_address = "127.0.0.1"  # single person 
port_no = 2525     # 0  - 65353


complete_address = (ip_address,port_no)
s.bind(complete_address)   

print("Hey i am reciving your messages .....")

while True:
    message = s.recvfrom(100)  
  # (b'lucknow', ('127.0.0.1', 58763))
    sender_address = message[1][0]   # '127.0.0.1'.txt
    sender_port_no = message[1][1]
    recived_message = message[0]

    decrypted_message = recived_message.decode('ascii')
    print(decrypted_message)
            # '127.0.0.1.txt'
    with open(sender_address +'.txt' , 'a+') as file:
        file.write(decrypted_message +'\n')








