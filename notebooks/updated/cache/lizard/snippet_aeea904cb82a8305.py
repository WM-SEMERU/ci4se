def add(self, intervention, name=None):
    if self.et is None:
        return
    assert isinstance(intervention, six.string_types)
    et = ElementTree.fromstring(intervention)
    vector_pop = VectorPopIntervention(et)
    assert isinstance(vector_pop.name, six.string_types)
    if name is not None:
        assert isinstance(name, six.string_types)
        et.attrib['name'] = name
    index = len(self.et.findall('intervention'))
    self.et.insert(index, et)