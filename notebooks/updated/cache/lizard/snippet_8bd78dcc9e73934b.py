def write(self, filename=None):
    if not filename:
        filename = self.filename
    self.properties.CurrentDate = _current_time()
    self.properties.EnableRubberBand = 'true'
    self.update_start_position()
    self.update_well_positions()
    self.update_counts()
    objectify.deannotate(self.root)
    for child in self.root.iterchildren():
        etree.cleanup_namespaces(child)
    xml = etree.tostring(self.root, encoding='utf8', xml_declaration=True,
        pretty_print=True)
    xml = '\r\n'.join(l.decode(encoding='utf8') for l in xml.splitlines())
    xml = re.sub('(["a-z])/>', '\\1 />', xml)
    xml = xml.replace("version='1.0' encoding='utf8'", 'version="1.0"')
    with open(filename, 'wb') as f:
        f.write(xml.encode('utf8'))