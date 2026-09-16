def readFd(fd, URL, encoding, options):
    ret = libxml2mod.xmlReadFd(fd, URL, encoding, options)
    if ret is None:
        raise treeError('xmlReadFd() failed')
    return xmlDoc(_obj=ret)