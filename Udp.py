
class Udp:

    def __init__(self, inPacket):
        self.inPacket = inPacket
        self.parse()

    def parse(self):
        self.sourcePort = int(int(self.inPacket[0] << 8) | int(self.inPacket[1]))
        self.destPort = int(int(self.inPacket[2] << 8) | int(self.inPacket[3]))
        self.length = int(int(self.inPacket[4] << 8) | int(self.inPacket[5]))
        self.checksum = int(int(self.inPacket[6] << 8) | int(self.inPacket[7]))
        self.payload = [ ]

    def getSourcePort(self):
        return self.sourcePort

    def getDestinationPort(self):
        return self.destPort

    def getLength(self):
        return self.length

    def getChecksum(self):
        return self.checksum

    def getPayload(self):
        return self.inPacket[8:]

    def dump(self, includePayload=True):
        print("------------------------------")
        print("Dumping UDP packet info")
        print("------------------------------")
        print("Source Port: {0}".format( self.sourcePort ))
        print("Destination Port: {0}".format( self.destPort ))
        print("Length: {0}".format( self.length ))
        print("Checksum: {0}".format( hex( self.checksum ) ))
        if includePayload:
            print("Payload")
            payloadStartIndex = 8
            payloadStr = "\n\t"
            for i in range(payloadStartIndex, self.length):
                payloadStr += "0x{:02x} ".format(self.inPacket[i])
                if not (i-(payloadStartIndex)+1) % 8:
                    payloadStr += "\n\t"
            print("{0}".format(payloadStr))

