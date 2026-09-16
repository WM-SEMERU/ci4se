def checkASN(filename):
    extnType = filename[filename.rfind('_') + 1:filename.rfind('.')]
    if isValidAssocExtn(extnType):
        return True
    else:
        return False