'''
This module provides basic functions.
'''

import os


def get_subdirs(sPath):
    '''
    Returns a list of subdirectories for a given path.

    Parameters:

      sPath: (string)

    Returns: list of strings
    '''
    lDirs = []
    for sName in os.listdir(sPath):
        sDir = os.path.join(sPath, sName)
        if os.path.isdir(sDir):
            lDirs.append(sDir)
    return lDirs


def subdir_has_init_file(sPath):
    '''
    Checks the for existence of __init__.py in the given path.

    Parameters:

      sPath: (string)

    Returns: boolean
    '''
    if '__init__.py' in os.listdir(sPath):
        return True
    else:
        return False 


def is_vhdl_file(sName):
    '''
    Checks if a file has the .vhd extension.

    Parameters:

      sName: (string)

    Returns: boolean
    '''
    if '.vhd' in sName:
        return True
    else:
        return False


def subdir_has_vhdl_file(sPath):
    '''
    Checks the for existence of vhdl files in the given path.

    Parameters:

      sPath: (string)

    Returns: boolean
    '''
    for sFile in os.listdir(sPath):
        if is_vhdl_file(sFile):
            return True
    return False 


def get_vhdl_files(sPath):
    '''
    Returns a list of vhdl files in the given path.

    Parameters:

      sPath: (string)

    Returns: (string list)
    '''
    lFiles = []
    for sFile in os.listdir(sPath):
        if is_vhdl_file(sFile):
            lFiles.append(sFile)
    return lFiles


def update_init_file(sPath, lVhdlFiles):
    '''
    Updates the __init__.py file.

    Parameters:

      sPath: (string)

      lVhdlFile: (string list)

    '''
    with open(os.path.join(sPath, '__init__.py'), 'w') as oFile:
        oFile.write('sDefaultLibrary = None\n')
        oFile.write('dFiles = {}\n')
        for sVhdlFile in lVhdlFiles:
            oFile.write('dFiles[\'' + sVhdlFile + '\'] = {}\n')
    oFile.close()
