def metadata(self):
    md = self.xml(src='docProps/core.xml')
    if md is None:
        md = XML(root=etree.Element('{%(cp)s}metadata' % self.NS))
    return md.root