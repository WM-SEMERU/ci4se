def parse(readDataInstance, nDebugEntries):
    dbgEntries = ImageDebugDirectories()
    dataLength = len(readDataInstance)
    toRead = nDebugEntries * consts.SIZEOF_IMAGE_DEBUG_ENTRY32
    if dataLength >= toRead:
        for i in range(nDebugEntries):
            dbgEntry = ImageDebugDirectory.parse(readDataInstance)
            dbgEntries.append(dbgEntry)
    else:
        raise excep.DataLengthException('Not enough bytes to read.')
    return dbgEntries