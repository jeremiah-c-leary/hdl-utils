
import os
import unittest

from hdl_utils.regfile import regfile as blah

from hdl_utils.tests.regfile import utils

sTestDir = os.path.dirname(__file__)

sTestFile = os.path.join(sTestDir, 'atxmega_spi.json')

oModel = blah.New(sTestFile)

lExpected  = utils.read_file(os.path.join(sTestDir, 'entity.expected.vhd'))


class test_entity(unittest.TestCase):


    def test_entity_generation(self):
        
        self.assertTrue(oModel)
        self.assertEqual('atxmega_spi', oModel.get_component_name())
        self.assertEqual(0, oModel.get_address_offset())
        self.assertEqual(4, len(oModel.get_children()))
        actualEntity = oModel.create_entity()
        lActual = actualEntity.render_to_list_of_strings()
        self.assertEqual(lExpected, lActual)
