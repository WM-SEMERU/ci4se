def _parseLoadConfigDirectory(self, rva, size, magic=consts.PE32):
    data = self.getDataAtRva(rva, directories.ImageLoadConfigDirectory().
        sizeof())
    rd = utils.ReadData(data)
    if magic == consts.PE32:
        return directories.ImageLoadConfigDirectory.parse(rd)
    elif magic == consts.PE64:
        return directories.ImageLoadConfigDirectory64.parse(rd)
    else:
        raise excep.InvalidParameterException('Wrong magic')