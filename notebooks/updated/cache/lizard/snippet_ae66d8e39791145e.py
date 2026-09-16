def parse(readDataInstance):
    if len(readDataInstance) == consts.IMAGE_NUMBEROF_DIRECTORY_ENTRIES * 8:
        newDataDirectory = DataDirectory()
        for i in range(consts.IMAGE_NUMBEROF_DIRECTORY_ENTRIES):
            newDataDirectory[i].name.value = dirs[i]
            newDataDirectory[i].rva.value = readDataInstance.readDword()
            newDataDirectory[i].size.value = readDataInstance.readDword()
    else:
        raise excep.DirectoryEntriesLengthException(
            'The IMAGE_NUMBEROF_DIRECTORY_ENTRIES does not match with the length of the passed argument.'
            )
    return newDataDirectory