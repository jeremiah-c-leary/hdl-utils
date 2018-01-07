
import unittest
import os

from hdl_utils import utils

sLocalPath = os.path.join('.', 'hdl_utils', 'tests', 'utils')


class testUtilsFunctions(unittest.TestCase):

    def test_is_vhdl_file(self):
        self.assertTrue(utils.is_vhdl_file('.vhd'))
        self.assertTrue(utils.is_vhdl_file('.vhdl'))
        self.assertFalse(utils.is_vhdl_file('.vho'))
        self.assertFalse(utils.is_vhdl_file('.txt'))

    def test_get_subdirs(self):
        self.assertEqual(utils.get_subdirs(sLocalPath), [os.path.join(sLocalPath, 'subdir1')])

        lExpected = []
        lExpected.append(os.path.join(sLocalPath, 'subdir1', 'subdir3'))
        lExpected.append(os.path.join(sLocalPath, 'subdir1', 'subdir2'))
        self.assertEqual(utils.get_subdirs(os.path.join(sLocalPath, 'subdir1')), lExpected)

        lExpected = []
        lExpected.append(os.path.join(sLocalPath, 'subdir1', 'subdir2', 'subdir2.1'))
        lExpected.append(os.path.join(sLocalPath, 'subdir1', 'subdir2', 'subdir2.2'))
        self.assertEqual(utils.get_subdirs(os.path.join(sLocalPath, 'subdir1', 'subdir2')), lExpected)

    def test_subdir_has_init_file(self):
        self.assertTrue(utils.subdir_has_init_file(os.path.join(sLocalPath, 'subdir1')))
        self.assertTrue(utils.subdir_has_init_file(os.path.join(sLocalPath, 'subdir1', 'subdir2')))
        self.assertTrue(utils.subdir_has_init_file(os.path.join(sLocalPath, 'subdir1', 'subdir2', 'subdir2.1')))
        self.assertFalse(utils.subdir_has_init_file(os.path.join(sLocalPath, 'subdir1', 'subdir2', 'subdir2.2')))
        self.assertTrue(utils.subdir_has_init_file(os.path.join(sLocalPath, 'subdir1', 'subdir3')))
        self.assertTrue(utils.subdir_has_init_file(os.path.join(sLocalPath, 'subdir1', 'subdir3', 'subdir3.1')))

    def test_subdir_has_vhdl_file(self):
        self.assertFalse(utils.subdir_has_vhdl_file(os.path.join(sLocalPath, 'subdir1')))
        self.assertFalse(utils.subdir_has_vhdl_file(os.path.join(sLocalPath, 'subdir1', 'subdir2')))
        self.assertTrue(utils.subdir_has_vhdl_file(os.path.join(sLocalPath, 'subdir1', 'subdir2', 'subdir2.1')))
        self.assertTrue(utils.subdir_has_vhdl_file(os.path.join(sLocalPath, 'subdir1', 'subdir2', 'subdir2.2')))
        self.assertFalse(utils.subdir_has_vhdl_file(os.path.join(sLocalPath, 'subdir1', 'subdir3')))
        self.assertTrue(utils.subdir_has_vhdl_file(os.path.join(sLocalPath, 'subdir1', 'subdir3', 'subdir3.1')))

    def test_get_vhdl_files(self):
        self.assertEqual(utils.get_vhdl_files(os.path.join(sLocalPath, 'subdir1')), [])
        self.assertEqual(utils.get_vhdl_files(os.path.join(sLocalPath, 'subdir1', 'subdir2')), [])
        self.assertEqual(utils.get_vhdl_files(os.path.join(sLocalPath, 'subdir1', 'subdir2', 'subdir2.1')), ['test.vhd'])
        self.assertEqual(utils.get_vhdl_files(os.path.join(sLocalPath, 'subdir1', 'subdir2', 'subdir2.2')), ['test.vhd'])
        self.assertEqual(utils.get_vhdl_files(os.path.join(sLocalPath, 'subdir1', 'subdir3')), [])
        self.assertEqual(utils.get_vhdl_files(os.path.join(sLocalPath, 'subdir1', 'subdir3', 'subdir3.1')), ['test.vhd'])
