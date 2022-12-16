from scapy.layers.inet import IP, ICMP
from scapy.layers.l2 import Ether
from scapy.sendrecv import srp1


pacote = Ether(src='10:05:01:9c:71:9e')
pacote /= IP(dst='172.18.5.1')
pacote /= ICMP()

resultado = srp1(pacote)

resultado.show()
