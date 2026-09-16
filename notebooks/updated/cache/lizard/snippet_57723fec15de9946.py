def convert_tree(self, element1, element2=None):
    if element2 is None:
        attributes = deepcopy(element1.attrib)
        tag = attributes['name']
        del attributes['name']
        element2 = etree.Element(tag, attributes)
    for e1 in element1.findall('node'):
        attributes = deepcopy(e1.attrib)
        tag = self.prefix_to_url(attributes['name'])
        del attributes['name']
        e2 = etree.SubElement(element2, tag, attributes)
        self.convert_tree(e1, e2)
    return element2