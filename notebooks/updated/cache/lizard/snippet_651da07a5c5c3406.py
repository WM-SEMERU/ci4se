def parse_property(self, tup_tree):
    self.check_node(tup_tree, 'PROPERTY', ('TYPE', 'NAME'), ('CLASSORIGIN',
        'PROPAGATED', 'EmbeddedObject', 'EMBEDDEDOBJECT', 'xml:lang'), (
        'QUALIFIER', 'VALUE'))
    attrl = attrs(tup_tree)
    try:
        val = self.unpack_value(tup_tree)
    except ValueError as exc:
        msg = str(exc)
        raise CIMXMLParseError(_format(
            "Cannot parse content of 'VALUE' child element of 'PROPERTY' element with name {0!A}: {1}"
            , attrl['NAME'], msg), conn_id=self.conn_id)
    qualifiers = self.list_of_matching(tup_tree, ('QUALIFIER',))
    embedded_object = False
    if 'EmbeddedObject' in attrl or 'EMBEDDEDOBJECT' in attrl:
        try:
            embedded_object = attrl['EmbeddedObject']
        except KeyError:
            embedded_object = attrl['EMBEDDEDOBJECT']
    if embedded_object:
        val = self.parse_embeddedObject(val)
    return CIMProperty(attrl['NAME'], val, type=attrl['TYPE'], is_array=
        False, class_origin=attrl.get('CLASSORIGIN', None), propagated=self
        .unpack_boolean(attrl.get('PROPAGATED', 'false')), qualifiers=
        qualifiers, embedded_object=embedded_object)