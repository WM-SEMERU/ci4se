def parse_value_namedinstance(self, tup_tree):
    self.check_node(tup_tree, 'VALUE.NAMEDINSTANCE')
    k = kids(tup_tree)
    if len(k) != 2:
        raise CIMXMLParseError(_format(
            'Element {0!A} has invalid number of child elements {1!A} (expecting two child elements (INSTANCENAME, INSTANCE))'
            , name(tup_tree), k), conn_id=self.conn_id)
    inst_path = self.parse_instancename(k[0])
    instance = self.parse_instance(k[1])
    instance.path = inst_path
    return instance