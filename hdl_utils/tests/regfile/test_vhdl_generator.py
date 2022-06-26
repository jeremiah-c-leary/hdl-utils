
import os
import unittest

from hdl_utils.regfile.model import memory_map

from hdl_utils.tests.regfile import utils

from hdl_utils.regfile.generator.vhdl import entity_generator
from hdl_utils.regfile.generator.vhdl import architecture_generator

sTestDir = os.path.dirname(__file__)

sTestFile = os.path.join(sTestDir, 'atxmega_spi.json')

oModel = memory_map.New(sTestFile)

lExpected_entity  = utils.read_file(os.path.join(sTestDir, 'entity.expected.vhd'))

lExpected_architecture  = utils.read_file(os.path.join(sTestDir, 'architecture.expected.vhd'))


class test_generator(unittest.TestCase):


    def test_entity_generation(self):
        
        lActual = entity_generator.generate(oModel)
        self.assertEqual(lExpected_entity, lActual)

    def test_architecture_generation(self):
        
        lActual = architecture_generator.generate(oModel)
        self.assertEqual(lExpected_architecture, lActual)


