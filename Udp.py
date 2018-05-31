
class Udp:

    def __init__(self, payload):
        self.payload = payload

    def dump(self):
        print("------------------------------")
        print("Dumping UDP packet info")
        print("------------------------------")
        sourcePort = int(int(self.payload[0] << 8) | int(self.payload[1]))
        destPort = int(int(self.payload[2] << 8) | int(self.payload[3]))
        length = int(int(self.payload[4] << 8) | int(self.payload[5]))
        checksum = int(int(self.payload[6] << 8) | int(self.payload[7]))
        print("Source Port: {0}".format( sourcePort ))
        print("Destination Port: {0}".format( destPort ))
        print("Length: {0}".format( length ))
        print("Checksum: {0}".format( hex( checksum ) ))
        print("Payload")
        payloadStartIndex = 8
        payloadStr = "\n\t"
        for i in range(payloadStartIndex, length):
            payloadStr += "0x{:02x} ".format(self.payload[i])
            if not (i-(payloadStartIndex)+1) % 8:
                payloadStr += "\n\t"
        print("{0}".format(payloadStr))

