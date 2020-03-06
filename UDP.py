import socket

def initializeSocket():
    # ~ UDP_IP = "192.168.1.20"
    UDP_IP = "192.168.43.144"
    UDP_PORT = 5005

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    return sock
    
def recvData(data):
    arr = ((data.decode()).split(" "))
    for i in range(0, len(arr)):
        arr[i] = int(arr[i])

    return arr
