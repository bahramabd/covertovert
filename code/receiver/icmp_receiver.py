import scapy
from scapy.all import IP, ICMP, sniff 

def process_packet(packet):
    if IP in packet and ICMP in packet and packet[IP].ttl == 1:
        print("[INFO] ICMP request received with TTL=1")
        packet.show()  # showing  details of the packet here 

def receive_icmp():
    print("[INFO] Listening for ICMP packets...")
    # here the code waits for the packet to be sent.
    sniff(filter="icmp", prn=process_packet)

if __name__ == "__main__":
    receive_icmp()