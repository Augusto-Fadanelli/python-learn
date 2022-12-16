from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import srp1


'''
who has 172.18.5.1
'''

MAC = '10:05:01:9c:71:9e'
BRD = 'ff:ff:ff:ff:ff:ff'

frame = Ether(src=MAC, dst=BRD)

pacote = ARP(pdst='172.18.5.1')

pacote_final = frame / pacote
pacote_final.show()

resposta = srp1(pacote_final)
resposta.show()
