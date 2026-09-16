def attr(self, name):
    nodes = self._do_query(multiple=False)
    val = self.poco.agent.hierarchy.getAttr(nodes, name)
    if six.PY2 and isinstance(val, six.text_type):
        val = val.encode('utf-8')
    return val