def parse_instance(self, tup_tree):
    self.check_node(tup_tree, 'INSTANCE', ('CLASSNAME',), ('xml:lang',), (
        'QUALIFIER', 'PROPERTY', 'PROPERTY.ARRAY', 'PROPERTY.REFERENCE'))
    qualifiers = self.list_of_matching(tup_tree, ('QUALIFIER',))
    props = self.list_of_matching(tup_tree, ('PROPERTY.REFERENCE',
        'PROPERTY', 'PROPERTY.ARRAY'))
    obj = CIMInstance(attrs(tup_tree)['CLASSNAME'], qualifiers=qualifiers)
    for prop in props:
        obj.__setitem__(prop.name, prop)
    return obj