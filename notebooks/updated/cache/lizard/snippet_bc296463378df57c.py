def fromString(self, inString):
    box = parseString(inString)[0]
    return Identifier(shareID=box['shareID'].decode('utf-8'), localpart=box
        ['localpart'].decode('utf-8'), domain=box['domain'].decode('utf-8'))