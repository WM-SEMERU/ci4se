def readerForMemory(buffer, size, URL, encoding, options):
    ret = libxml2mod.xmlReaderForMemory(buffer, size, URL, encoding, options)
    if ret is None:
        raise treeError('xmlReaderForMemory() failed')
    return xmlTextReader(_obj=ret)