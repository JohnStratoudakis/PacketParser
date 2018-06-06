import unittest

# +----------------------------------------------------------------------------+
# |         Source Port                 |         Destination Port             |
# +----------------------------------------------------------------------------+
# |         Checksum                    |         Total Length                 |
# +----------------------------------------------------------------------------+
# |                              Payload                                       |
# +----------------------------------------------------------------------------+

from Udp import Udp

class UdpTests(unittest.TestCase):

    def test_packet(self):
        # GIVEN
        packet = [
            0x14, 0xe9, 0x14, 0xe9, 0x00, 0x46, 0x64, 0xbe,
            0x00, 0x00, 0x84, 0x00, 0x00, 0x00, 0x00, 0x01,
            0x00, 0x00, 0x00, 0x00, 0x03, 0x31, 0x30, 0x30,
            0x01, 0x31, 0x01, 0x30, 0x02, 0x31, 0x30, 0x07,
            0x69, 0x6e, 0x2d, 0x61, 0x64, 0x64, 0x72, 0x04,
            0x61, 0x72, 0x70, 0x61, 0x00, 0x00, 0x0c, 0x80,
            0x01, 0x00, 0x00, 0x00, 0x78, 0x00, 0x0f, 0x07,
            0x6c, 0x69, 0x6e, 0x75, 0x78, 0x2d, 0x36, 0x05,
            0x6c, 0x6f, 0x63, 0x61, 0x6c, 0x00
            ]

        # WHEN
        udp = Udp(packet)

        # THEN
        self.assertEqual(udp.getSourcePort(), 5353)
        self.assertEqual(udp.getDestinationPort(), 5353)
        self.assertEqual(udp.getLength(), 70)
        self.assertEqual(udp.getChecksum(), 0x64be)
        self.assertEqual(udp.getPayload()[0], 0x0)

    def test_smoke(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()