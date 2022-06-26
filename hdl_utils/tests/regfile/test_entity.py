
import os
import unittest

from hdl_utils.regfile.model import memory_map

from hdl_utils.tests.regfile import utils

from hdl_utils.regfile.generator.vhdl import entity_generator

sTestDir = os.path.dirname(__file__)

sTestFile = os.path.join(sTestDir, 'atxmega_spi.json')

oModel = memory_map.New(sTestFile)

lExpected  = utils.read_file(os.path.join(sTestDir, 'entity.expected.vhd'))


class test_entity(unittest.TestCase):


    def test_entity_generation(self):
        
        self.assertTrue(oModel)
        self.assertEqual('atxmega_spi', oModel.get_component_name())
        self.assertEqual(0, oModel.get_address_offset())
        self.assertEqual(4, len(oModel.get_children()))
        lActual = entity_generator.generate(oModel)
#        actualEntity = oModel.create_entity()
#        lActual = actualEntity.render_to_list_of_strings()
        self.assertEqual(lExpected, lActual)
