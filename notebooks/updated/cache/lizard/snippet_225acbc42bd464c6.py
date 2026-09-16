def toXml(self, xparent):
    for key, value in self.items():
        elem = ElementTree.SubElement(xparent, 'entry')
        typ = type(elem).__name__
        elem.set('key', key)
        elem.set('type', typ)
        if typ in DataSet._xmlTypes:
            DataSet._xmlTypes[typ][0](elem, value)
        else:
            elem.set('value', nstr(value))