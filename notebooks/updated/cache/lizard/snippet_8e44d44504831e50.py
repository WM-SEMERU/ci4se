def get_ancestors(self, obj):

    def _get_ancestors(code, needle):
        for node in code.nodes:
            if node is needle:
                return []
            for code in node.__children__():
                ancestors = _get_ancestors(code, needle)
                if ancestors is not None:
                    return [node] + ancestors
    if isinstance(obj, Wikicode):
        obj = obj.get(0)
    elif not isinstance(obj, Node):
        raise ValueError(obj)
    ancestors = _get_ancestors(self, obj)
    if ancestors is None:
        raise ValueError(obj)
    return ancestors