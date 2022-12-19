from scapy.config import conf
from scapy.arch.common import get_if_raw_hwaddr
from scapy.layers.inet import IP, UDP
from scapy.layers.l2 import Ether
from scapy.layers.dhcp import BOOTP, DHCP
from scapy.sendrecv import sendp, srp1, AsyncSniffer
from scapy.volatile import RandInt


meu_mac = get_if_raw_hwaddr(conf.iface)[1]
#print(meu_mac)
print(conf.iface)

def dhcp_discover():
    pacote = Ether(src=conf.iface.mac)
    pacote = IP(src='0.0.0.0', dst='255.255.255.255')
    pacote /= UDP(sport=68, dport=67)
    pacote /= BOOTP(chaddr=meu_mac, xid=RandInt())
    pacote /= DHCP(options=[('message-type', 'discover'), 'end'])
    sendp(pacote, iface=conf.iface)
    #r = srp1(pacote)

from time import sleep
s = AsyncSniffer(filter='udp and port 68')
s.start()
sleep(0.5)
dhcp_discover()
sleep(2)
s.stop()

print(s.results.show())
print(s.results)
