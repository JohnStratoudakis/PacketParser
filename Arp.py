
#packet = [
#   0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x02,
#   0xc9, 0x55, 0x08, 0x44, 0x08, 0x06, 
# 
# HTYPE - 0x00, 0x01,
# PTYPE - 0x08, 0x00,
# HLEN - 0x06,
# PLEN - 0x04,
# OPER - 0x00, 0x01,
# SHA - 0x00, 0x02, 0xc9, 0x55, 0x08, 0x44,
# SPA -  0x0a, 0x00, 0x01, 0x64,
# THA - 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
# TPA - 0x0a, 0x00, 0x01, 0x65,
# Padding
# 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
# 0x00, 0x00, 0x00, 0x00, 0x7c, 0xe0, 0xaf, 0xe2,
#]

class Arp:

    def __init__(self, inPayload):
        self.payload = inPayload

    def dump(self):
        print("------------------------------")
        print("Dumping ARP packet info")
        print("------------------------------")
        print("HTYPE: {0}".format( self.payload[0:2]))
        print("PTYPE: {0}".format( self.payload[2:4]))
        print("HLEN: {0}".format( self.payload[4]))
        print("PLEN: {0}".format( self.payload[5]))
        print("OPER: {0}".format( self.payload[6:8]))
        print("SHA: {0}".format( " ".join(  map(hex, map(int,self.payload[8:14]))) ))
        print("SPA: {0}".format( self.payload[14:18]) )
        print("THA: {0}".format( " ".join(  map(hex, map(int,self.payload[18:24]))) ))
        print("TPA: {0}".format( self.payload[24:26]) )

