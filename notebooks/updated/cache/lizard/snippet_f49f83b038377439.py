def save(self):
    if self.rater is not None:
        self.rater.set('modified', datetime.now().isoformat())
    xml = parseString(tostring(self.root))
    with open(self.xml_file, 'w') as f:
        f.write(xml.toxml())