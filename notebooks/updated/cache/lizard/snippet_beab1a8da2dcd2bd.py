def save(self, filename, encoding='ISO-8859-1', standalone='no'):
    f = codecs.open(filename, 'w', encoding)
    s = self.wrap_xml(self.getXML(), encoding, standalone)
    f.write(s)
    f.close()