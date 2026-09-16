def URIUnescapeString(str, len, target):
    ret = libxml2mod.xmlURIUnescapeString(str, len, target)
    return ret