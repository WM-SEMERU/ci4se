def create(self, name, site_element):
    site_element = element_resolver(site_element)
    json = {'name': name, 'site_element': site_element}
    return ElementCreator(self.__class__, href=self.href, json=json)