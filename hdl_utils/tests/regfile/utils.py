
def read_file(sFilename):
    lLines = []
    with open(sFilename) as oFile:
        for sLine in oFile:
            lLines.append(sLine.rstrip())
    return lLines
