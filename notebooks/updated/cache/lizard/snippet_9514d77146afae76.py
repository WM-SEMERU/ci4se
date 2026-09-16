def parseXRDS(text):
    try:
        bytestring = text.encode('utf8') if isinstance(text, str) else text
        element = SafeElementTree.XML(bytestring)
    except (SystemExit, MemoryError, AssertionError, ImportError):
        raise
    except Exception as why:
        exc = XRDSError('Error parsing document as XML')
        exc.reason = why
        raise exc
    else:
        tree = ElementTree.ElementTree(element)
        if not isXRDS(tree):
            raise XRDSError('Not an XRDS document')
        return tree