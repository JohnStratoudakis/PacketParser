
#  0x00, 0x5e, 0x00, 0x01, 0x02, 0x00, 0xfb, 0x00,
#  0x44, 0x08, 0x55, 0xc9, 0x00, 0x45, 0x00, 0x08,
#  0x42, 0x63, 0x5a, 0x00, 0x11, 0xff, 0x00, 0x40,
#  0x00, 0x0a, 0xf1, 0x2b, 0x00, 0xe0, 0x64, 0x01,
#  0xe9, 0x14, 0xfb, 0x00, 0x46, 0x00, 0xe9, 0x14,
#  0x00, 0x00, 0xbe, 0x64, 0x00, 0x00, 0x00, 0x84,
#  0x00, 0x00, 0x01, 0x00, 0x31, 0x03, 0x00, 0x00,
#  0x31, 0x01, 0x30, 0x30, 0x31, 0x02, 0x30, 0x01,
#  0x6e, 0x69, 0x07, 0x30, 0x64, 0x64, 0x61, 0x2d,
#  0x72, 0x61, 0x04, 0x72, 0x00, 0x00, 0x61, 0x70,
#  0x00, 0x01, 0x80, 0x0c, 0x00, 0x78, 0x00, 0x00,
#  0x69, 0x6c, 0x07, 0x0f, 0x2d, 0x78, 0x75, 0x6e,
#  0x6f, 0x6c, 0x05, 0x36, 0x00, 0x6c, 0x61, 0x63
#
# 
class IPv4:

    def __init__(self, inPayload):
        self.payload = inPayload

    def getProtocol(self):
        return self.payload[9]

    def getProtocolStr(self):
        protocolStr = "{0}".format( self.payload[9] )
        if self.payload[9] == 1:
            protocolStr += " ICMP"
        elif self.payload[9] == 2:
            protocolStr += " IGMP"
        elif self.payload[9] == 6:
            protocolStr += " TCP"
        elif self.payload[9] == 17:
            protocolStr += " UDP"
        else:
            protocolStr += " (Unknown)"
        return protocolStr

    def getPayload(self):
        payloadStartIndex = 20
        totalLength = (self.payload[2] << 8) | self.payload[3]
        dataPayload = self.payload[payloadStartIndex:totalLength]
        return dataPayload

    def dump(self):
        print("------------------------------")
        print("Dumping IPV4 packet info")
        print("------------------------------")
        print("Version: {0}".format( hex( (self.payload[0] & 0xF0)>> 4)) )
        # IHL number of 32 bit words for header length
        IHL = (self.payload[0] & 0xF)
        print("IHL: {0}".format( hex( IHL ) ) )
        print("IHL: {0}".format( hex( self.payload[0] & 0xF) ) )
        print("DSCP: {0}".format( hex( self.payload[1] & 0xF) ) )
        print("ECN: {0}".format( hex( self.payload[1] & 0xF) ) )
        totalLength = (self.payload[2] << 8) | self.payload[3]
        print("Total Length: {0} ({1})".format( hex(totalLength), totalLength))
        print("Identification: {0}".format( hex (
            (self.payload[4] << 8) | self.payload[5]
        )))
        print("Flags: {0}".format( hex (
            (self.payload[6] & 0xE0)
        )))
        print("Fragment Offset: {0}".format( hex (
            ((self.payload[6] & 0x10) << 8)| (self.payload[7])
        )))
        print("Time to Live: {0}".format( hex (
            (self.payload[8])
        )))
        protocolStr = self.getProtocolStr()
        print("Protocol: {0}".format( protocolStr ))
        print("Header Checksum: {0}".format( hex (
            (self.payload[10] << 8)| (self.payload[11])
        )))
        print("Source IP Address: {0}.{1}.{2}.{3}".format( self.payload[12], self.payload[13], self.payload[14], self.payload[15]))
        print("Destination IP Address: {0}.{1}.{2}.{3}".format( self.payload[16], self.payload[17], self.payload[18], self.payload[19]))
        payloadStartIndex = 20
        if IHL > 5:
            print("IHL is greater than 5")
        print("Payload")
        payloadStr = "\n\t"
        for i in range(payloadStartIndex, totalLength - 0):
            payloadStr += "0x{:02x} ".format(self.payload[i])
            if not (i-(payloadStartIndex)+1) % 8:
                payloadStr += "\n\t"
        print("{0}".format(payloadStr))
