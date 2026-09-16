def parse_multireq(self, tup_tree):
    raise CIMXMLParseError(_format(
        'Internal Error: Parsing support for element {0!A} is not implemented',
        name(tup_tree)), conn_id=self.conn_id)