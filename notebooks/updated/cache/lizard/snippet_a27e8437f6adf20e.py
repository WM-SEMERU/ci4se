def simple_value(self, elt, ps, mixed=False):
    if not _valid_encoding(elt):
        raise EvaluateException('Invalid encoding', ps.Backtrace(elt))
    c = _children(elt)
    if mixed is False:
        if len(c) == 0:
            raise EvaluateException('Value missing', ps.Backtrace(elt))
        for c_elt in c:
            if c_elt.nodeType == _Node.ELEMENT_NODE:
                raise EvaluateException('Sub-elements in value', ps.
                    Backtrace(c_elt))
    return ''.join([E.nodeValue for E in c if E.nodeType in [_Node.
        TEXT_NODE, _Node.CDATA_SECTION_NODE]])