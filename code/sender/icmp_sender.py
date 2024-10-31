import scapy
from scapy.all import IP, ICMP, send

def send_icmp():
    # creating packet here
    packet = IP(dst="receiver", ttl=1) / ICMP()
    print("[INFO] Sending ICMP packet with TTL=1 to receiver...")
    
    # sending the packet
    send(packet)
    print("[INFO] Packet sent.")

if __name__ == "__main__":
    send_icmp()
