def open(self, append: bool=False, write: bool=False):
    flag = {(False, False): 'r', (True, False): 'a', (True, True): 'a', (
        False, True): 'w'}[append, write]
    realPath = self.realPath
    realDir = os.path.dirname(realPath)
    if not os.path.exists(realDir):
        os.makedirs(realDir, DirSettings.defaultDirChmod)
    return open(self.realPath, flag)