
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

    def joinTo16(self, hi, lo):
        return (hi << 8) | (lo)

    def __init__(self, inPayload):
        self.payload = inPayload
        self.parse()

    def parse(self):
        self.htype = self.joinTo16(self.payload[0], self.payload[1])
        self.ptype = self.joinTo16(self.payload[2], self.payload[3])
        self.hlen = self.payload[4]
        self.plen = self.payload[5]
        self.oper = self.joinTo16(self.payload[6], self.payload[7])
        self.sha = self.payload[8:14]
        self.spa = self.payload[14:18]
        self.tha = self.payload[18:24]
        self.tpa = self.payload[24:26]

    def dump(self):
        print("------------------------------")
        print("Dumping ARP packet info")
        print("------------------------------")
        print("HTYPE: {0}".format( self.htype ))
        print("PTYPE: {0}".format( self.ptype ))
        print("HLEN: {0}".format( self.hlen ))
        print("PLEN: {0}".format( self.plen ))
        print("OPER: {0}".format( self.oper ))
        print("SHA: {0}".format( " ".join(  map(hex, map(int,self.payload[8:14]))) ))
        print("SPA: {0}".format( self.payload[14:18]) )
        print("THA: {0}".format( " ".join(  map(hex, map(int,self.payload[18:24]))) ))
        print("TPA: {0}".format( self.payload[24:26]) )
