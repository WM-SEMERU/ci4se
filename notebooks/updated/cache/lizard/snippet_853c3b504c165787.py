def create_namedlayer(self, name):
    namedlayer = self.get_or_create_element('sld', 'NamedLayer')
    namedlayer.Name = name
    return namedlayer