from socket import *
import time


#Plhrofories gia to pou tha ginei to Ping 
serverName = '127.0.0.1'
serverPort = 12000

serverAddress=(serverName , serverPort)
#Dhmiourgoume to socket 
clientSocket = socket(AF_INET, SOCK_DGRAM)

#Set timeout gia 1 deuterolepto
clientSocket.settimeout(1)

for sequence_number in range(1, 11):
    
    #Dhmiourgia tou Messeage
    send_time = time.time()
    message = f"Ping {sequence_number} {send_time}"
    
    try:
        #Apostolh UDP
        clientSocket.sendto(message.encode(), (serverAddress))
        
        #Perimenei apanthsh
        response, serverAddress = clientSocket.recvfrom(1024)
        receive_time = time.time()
        
        # Ypologismos RTT
        rtt = receive_time - send_time
        
        print(f"Reply from {serverName}: {response.decode()}")
        print(f"RTT = {rtt:.6f} seconds\n")

    #Excpetion gia time out
    except timeout:
        print("Request timed out\n")

#Kleisimo tou socket
clientSocket.close()