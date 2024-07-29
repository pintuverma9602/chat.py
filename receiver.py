import socket
from datetime import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_address="127.0.0.1"
port_no=2121
complete_address= (ip_address,port_no)
s.bind(complete_address)
    
print("Hey i am listening......")
while True:
        Data = s.recvfrom(100)
        message = Data[0].decode('ascii')
        sender_ip_address = Data[1][0]
        file = open(sender_ip_address + '.txt', 'a')
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# Combine the message with the current date and time
        message_with_datetime = f"{"Your current date and time is : ",current_datetime} : {"Your message is:",message}"
        file.write(message_with_datetime)
        file.write("\n")
        print(message)
        file.close()
        # this is the thank you msg ,to be send to the sender
        sender_address=Data[1]
        s.sendto(b"thank you!!!For your message!",sender_address)

 