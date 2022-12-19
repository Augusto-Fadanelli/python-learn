from scapy.config import conf
from scapy.sendrecv import AsyncSniffer
from time import sleep


s = AsyncSniffer(filter='udp and port 68', iface=conf.iface)
s.start()

sleep(5)

s.stop()
print(s.results)
