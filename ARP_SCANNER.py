from scapy.all import Ether,ARP,srp
# first we trying to build ethernet packet using scapy library

ether_header=Ether(dst="FF:FF:FF:FF:FF:FF")
ip_range=input("enter your ips> ")
arp_options=ARP(pdst=ip_range)
arp_packet=ether_header /arp_options

result, noresult=srp(arp_packet,timeout=2)
print("")
print("live pcs are : ")
print("********************")


for send,recieve in result:
    print (recieve[Ether].psrc,recieve[Ether].hwsrc)

