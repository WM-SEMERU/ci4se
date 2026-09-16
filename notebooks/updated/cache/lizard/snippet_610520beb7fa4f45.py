def htmlReadFile(filename, encoding, options):
    ret = libxml2mod.htmlReadFile(filename, encoding, options)
    if ret is None:
        raise treeError('htmlReadFile() failed')
    return xmlDoc(_obj=ret)