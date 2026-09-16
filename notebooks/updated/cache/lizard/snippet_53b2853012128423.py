def _getSuitableClasses(self, data, imageDosHeader):
    classes = None
    machine = IMAGE_FILE_MACHINE[c_ushort.from_buffer(data, imageDosHeader.
        header.e_lfanew + 4).value]
    if machine == IMAGE_FILE_MACHINE.I386:
        classes = PE32
    elif machine == IMAGE_FILE_MACHINE.AMD64:
        classes = PE64
    return classes