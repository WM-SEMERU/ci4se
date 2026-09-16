def htmlCreatePushParser(SAX, chunk, size, URI):
    ret = libxml2mod.htmlCreatePushParser(SAX, chunk, size, URI)
    if ret is None:
        raise parserError('htmlCreatePushParser() failed')
    return parserCtxt(_obj=ret)