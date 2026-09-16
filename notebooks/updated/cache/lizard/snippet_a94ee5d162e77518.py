def parseFile(filename):
    ret = libxml2mod.xmlParseFile(filename)
    if ret is None:
        raise parserError('xmlParseFile() failed')
    return xmlDoc(_obj=ret)