def parse(readDataInstance):
    dbgDir = ImageDebugDirectory()
    dbgDir.characteristics.value = readDataInstance.readDword()
    dbgDir.timeDateStamp.value = readDataInstance.readDword()
    dbgDir.majorVersion.value = readDataInstance.readWord()
    dbgDir.minorVersion.value = readDataInstance.readWord()
    dbgDir.type.value = readDataInstance.readDword()
    dbgDir.sizeOfData.value = readDataInstance.readDword()
    dbgDir.addressOfData.value = readDataInstance.readDword()
    dbgDir.pointerToRawData.value = readDataInstance.readDword()
    return dbgDir