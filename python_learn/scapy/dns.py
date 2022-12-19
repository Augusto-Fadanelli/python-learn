from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import IP, UDP
#from scapy.layers.l2 import Ether
from scapy.sendrecv import sr1 # Send Receive 1


#pacote = Ether() # Endereço físico
pacote = IP(dst='8.8.8.8') # Endereço virtual
pacote /= UDP(dport=53) # Porta do serviço
pacote /= DNS(qd=DNSQR(qname='google.com')) # Protocolo do serviço

resposta = sr1(pacote)
resposta.show()
