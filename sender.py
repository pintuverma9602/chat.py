import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Replace with the IP address of the receiver
target_ip = "127.0.0.1"
target_port = 2121
target_address = (target_ip, target_port)

condition = True
while condition:
    message = input("Please enter your message: ")
    message_encoded = message.encode('ascii')

    s.sendto(message_encoded, target_address)
    print("Your message has been sent.")

    # Receive the "thank you" message
    data, address = s.recvfrom(1024)
    thank_you_message = data.decode('ascii')
    print(f"Received: {thank_you_message}")

    permission = input("Do you want to quit the program? (Press Y/N): ")
    if permission.upper() == "Y":
       condition = False
 