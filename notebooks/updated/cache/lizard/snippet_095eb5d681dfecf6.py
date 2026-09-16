def optional_child(self, tup_tree, allowed):
    k = kids(tup_tree)
    if not k:
        return None
    if len(k) == 1:
        return self.one_child(tup_tree, allowed)
    raise CIMXMLParseError(_format(
        'Element {0!A} has too many child elements {1!A} (allowed is one optional child element {2!A})'
        , name(tup_tree), [name(t) for t in k], allowed), conn_id=self.conn_id)