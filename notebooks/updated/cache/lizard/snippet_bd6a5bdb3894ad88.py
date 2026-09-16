def to_str(self):
    return etree.tostring(self.root, xml_declaration=True, standalone=True,
        pretty_print=True)