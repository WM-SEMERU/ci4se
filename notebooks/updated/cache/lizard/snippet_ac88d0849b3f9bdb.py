def _parseBoundImportDirectory(self, rva, size, magic=consts.PE32):
    data = self.getDataAtRva(rva, size)
    rd = utils.ReadData(data)
    boundImportDirectory = directories.ImageBoundImportDescriptor.parse(rd)
    for i in range(len(boundImportDirectory) - 1):
        if hasattr(boundImportDirectory[i], 'forwarderRefsList'):
            if boundImportDirectory[i].forwarderRefsList:
                for forwarderRefEntry in boundImportDirectory[i
                    ].forwarderRefsList:
                    offset = forwarderRefEntry.offsetModuleName.value
                    forwarderRefEntry.moduleName = self.readStringAtRva(
                        offset + rva)
        offset = boundImportDirectory[i].offsetModuleName.value
        boundImportDirectory[i].moduleName = self.readStringAtRva(offset + rva)
    return boundImportDirectory