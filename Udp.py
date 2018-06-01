
class Udp:

    def __init__(self, payload):
        self.payload = payload
        self.parse()

    def parse(self):
        self.sourcePort = int(int(self.payload[0] << 8) | int(self.payload[1]))
        self.destPort = int(int(self.payload[2] << 8) | int(self.payload[3]))
        self.length = int(int(self.payload[4] << 8) | int(self.payload[5]))
        self.checksum = int(int(self.payload[6] << 8) | int(self.payload[7]))

    def getSourcePort(self):
        return self.sourcePort
    
    def getDestinationPort(self):
        return self.destPort

    def getLength(self):
        return self.length

    def getChecksum(self):
        return self.checksum

    def dump(self):
        print("------------------------------")
        print("Dumping UDP packet info")
        print("------------------------------")
        #sourcePort = int(int(self.payload[0] << 8) | int(self.payload[1]))
        #destPort = int(int(self.payload[2] << 8) | int(self.payload[3]))
        #length = int(int(self.payload[4] << 8) | int(self.payload[5]))
        #checksum = int(int(self.payload[6] << 8) | int(self.payload[7]))
        print("Source Port: {0}".format( self.sourcePort ))
        print("Destination Port: {0}".format( self.destPort ))
        print("Length: {0}".format( self.length ))
        print("Checksum: {0}".format( hex( self.checksum ) ))
        print("Payload")
        payloadStartIndex = 8
        payloadStr = "\n\t"
        for i in range(payloadStartIndex, self.length):
            payloadStr += "0x{:02x} ".format(self.payload[i])
            if not (i-(payloadStartIndex)+1) % 8:
                payloadStr += "\n\t"
        print("{0}".format(payloadStr))

