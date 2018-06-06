#!/usr/bin/python

from Ethernet import Ethernet
from Arp import Arp
from IPv4 import IPv4
from Udp import Udp

packet = [ 
  0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x01, 
  0x02, 0x03, 0x04, 0x05, 0x08, 0x06, 0x00, 0x01, 
  0x08, 0x00, 0x06, 0x04, 0x00, 0x01, 0x00, 0x01, 
  0x02, 0x03, 0x04, 0x05, 0x0a, 0x00, 0x01, 0x65, 
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0a, 0x00, 
  0x01, 0x65
]

# 94  tapif_select::New Packet received of size: 68
# 95   Before byte re-ordering
# 96   0xff, 0xff, 0xff, 0xff, 0x02, 0x00, 0xff, 0xff,
# 97   0x44, 0x08, 0x55, 0xc9, 0x01, 0x00, 0x06, 0x08,
# 98   0x04, 0x06, 0x00, 0x08, 0x02, 0x00, 0x01, 0x00,
# 99   0x44, 0x08, 0x55, 0xc9, 0x64, 0x01, 0x00, 0x0a,
#100   0x00, 0x00, 0x00, 0x00, 0x00, 0x0a, 0x00, 0x00,
#101   0x00, 0x00, 0x65, 0x01, 0x00, 0x00, 0x00, 0x00,
#102   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
#103   0x00, 0x00, 0x00, 0x00, 0xe2, 0xaf, 0xe0, 0x7c,
#104
#105 After byte re-ordering
#106   0x02, 0x00, 0x00, 0x00,
#107   0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x02,
#108   0xc9, 0x55, 0x08, 0x44, 0x08, 0x06, 0x00, 0x01,
#109   0x08, 0x00, 0x06, 0x04, 0x00, 0x01, 0x00, 0x02,
#110   0xc9, 0x55, 0x08, 0x44, 0x0a, 0x00, 0x01, 0x64,
#111   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0a, 0x00,
#112   0x01, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
#113   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
#114   0x00, 0x00, 0x00, 0x00, 0x7c, 0xe0, 0xaf, 0xe2,
#115   0x00, 0x00, 0x00, 0x02,

# First outgoing packet
packet = [
   0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x02,
   0xc9, 0x55, 0x08, 0x44, 0x08, 0x06, 0x00, 0x01,
   0x08, 0x00, 0x06, 0x04, 0x00, 0x01, 0x00, 0x02,
   0xc9, 0x55, 0x08, 0x44, 0x0a, 0x00, 0x01, 0x64,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0a, 0x00,
   0x01, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00 #, 0x7c, 0xe0, 0xaf, 0xe2,
]

# Incoming packet in reverse order (network byte order)
inPkt = [
  0xff, 0xff, 0xff, 0xff, 0x02, 0x00, 0xff, 0xff,
  0x44, 0x08, 0x55, 0xc9, 0x01, 0x00, 0x06, 0x08,
  0x04, 0x06, 0x00, 0x08, 0x02, 0x00, 0x01, 0x00,
  0x44, 0x08, 0x55, 0xc9, 0x64, 0x01, 0x00, 0x0a,
  0x00, 0x00, 0x00, 0x00, 0xd3, 0x8c, 0x00, 0x00,
  0x00, 0x00, 0xce, 0xa9, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0xd3, 0xaf, 0x48, 0x93
]

# Plan
# 1 - Are packets sent out of the lwip received on the other side? i.e. is the network byte order thing okay?
# 2 - Should I flip them in the microblaze? yes
# 00:02:c9:55:08:44
eth = Ethernet(packet)
eth.dump()
print("eth.etherType = {0}".format(hex(eth.getEtherType())))
if eth.getEtherType() == 0x800:
  ipv4 = IPv4(eth.getPayload())
  ipv4.dump()
  if ipv4.getProtocol() == 17:
    udp = Udp(ipv4.getPayload())
    udp.dump()
elif eth.getEtherType() == 0x806:
  arp = Arp(eth.getPayload())
  arp.dump()
