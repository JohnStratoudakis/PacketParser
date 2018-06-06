import unittest

# +----------------------------------------------------------------------------+
# |         Source Port                 |         Destination Port             |
# +----------------------------------------------------------------------------+
# |         Checksum                    |         Total Length                 |
# +----------------------------------------------------------------------------+
# |                              Payload                                       |
# +----------------------------------------------------------------------------+

from Arp import Arp 

class ArpTests(unittest.TestCase):

    def test_packet(self):
        # GIVEN
        packet = [
            0x00, 0x01, 0x08, 0x00, 0x06, 0x04, 0x00, 0x01,
            0x00, 0x02, 0xc9, 0x55, 0x08, 0x44, 0x0a, 0x00,
            0x01, 0x64, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x0a, 0x00, 0x01, 0x65, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00
        ]

        # WHEN
        arp = Arp(packet)

        # THEN
        self.assertEqual(arp.htype, 1)
