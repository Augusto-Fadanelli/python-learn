from scapy.config import conf
from scapy.sendrecv import sniff


def xpto(s):
    #return s.summary()
    return s.show()

try:
    sniff(filter='tcp', prn=xpto, iface=conf.iface)
except KeyboardInterrupt:
    exit(0)
