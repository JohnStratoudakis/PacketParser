
class Ethernet:

    def __init__(self, inPkt):
        self.inPkt = inPkt
        self.parse()

    def convertToHex(self, inList):
        return " ".join(  map(hex, map(int,inList)))

    def getDestMac(self):
        return self.convertToHex(self.destMac)

    def getSourceMac(self):
        return self.convertToHex(self.sourceMac)

    def getEtherTypeStr(self):
        etherType = int(int(self.etherType[0] << 8) | int(self.etherType[1]))
        res = "{0} ".format(str(hex(etherType)))
        if etherType == 0x806:
            res += "(ARP)"
        elif etherType == 0x800:
            res += "(IPv4)"
        return res

    def getEtherType(self):
        etherType = int(int(self.etherType[0] << 8) | int(self.etherType[1]))
        return etherType

    def parse(self):
        self.destMac = self.inPkt[0:6]
        self.sourceMac = self.inPkt[6:12]
        self.etherType = self.inPkt[12:14]
        self.payload = self.inPkt[14:]

    def getPayload(self):
        #return self.convertToHex(self.payload)
        return self.payload

    def dump(self):
        print("------------------------------")
        print("Dumping Ethernet Frame info")
        print("------------------------------")
        print("Dest MAC:   \t" + self.getDestMac())
        print("Source MAC: \t" + self.getSourceMac())
        print("EtherType:  \t" + self.getEtherTypeStr())
        print("Payload:")

        payloadStr = "\n\t"
        for x in range(len(self.payload)):
            payloadStr += "0x{:02x} ".format(self.payload[x])
            if not (x+1) % 8:
                payloadStr += "\n\t"

        print("{0}".format(payloadStr))
        bArr = bytes(self.inPkt)
        import zlib
        crc32 = zlib.crc32(bArr) & 0xFFFFFFFF
        print("CRC32: {0}".format( hex(crc32) ))
        print("Expected CRC: {0}".format( self.convertToHex( [0x7c, 0xe0, 0xaf, 0xe2] ) ))
