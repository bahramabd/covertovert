import scapy
from scapy.all import IP, ICMP, sniff 

def handle_packet(packet):
    if packet.haslayer("ICMP"):
        print("Received ICMP packet:")
        packet.show()

print("Listening for ICMP packets...")
#sniff(filter="icmp", prn=handle_packet, count=1)
print("Exiting after receiving the first ICMP packet.")