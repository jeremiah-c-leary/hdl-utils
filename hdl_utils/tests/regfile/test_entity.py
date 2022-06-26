
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
        
        lActual = entity_generator.generate(oModel)
        self.assertEqual(lExpected, lActual)


