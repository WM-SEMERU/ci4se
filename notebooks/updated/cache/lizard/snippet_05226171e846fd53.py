def fromstring(cls, string):
    parser = etree.XMLParser(remove_blank_text=True)
    root = etree.fromstring(string, parser)
    tree = root.getroottree()
    return cls.fromtree(tree)