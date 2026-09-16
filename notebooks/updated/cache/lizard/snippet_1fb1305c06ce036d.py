def security_iter(nodearr):
    assert nodearr.name() == 'securityData' and nodearr.isArray()
    for i in range(nodearr.numValues()):
        node = nodearr.getValue(i)
        err = XmlHelper.get_security_error(node)
        result = (None, err) if err else (node, None)
        yield result