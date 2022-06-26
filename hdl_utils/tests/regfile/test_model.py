
import os
import unittest

from hdl_utils.regfile.model import memory_map

sTestDir = os.path.dirname(__file__)

sTestFile = os.path.join(sTestDir, 'atxmega_spi.json')

oModel = memory_map.New(sTestFile)

class test_entity(unittest.TestCase):


    def test_entity_generation(self):
        
        self.assertTrue(oModel)
        self.assertEqual('atxmega_spi', oModel.get_component_name())
        self.assertEqual(0, oModel.get_address_offset())
        self.assertEqual(4, len(oModel.get_children()))


