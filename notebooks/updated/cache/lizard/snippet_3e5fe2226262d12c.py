def _fixed_source_line(self):
    line = self.lineno
    _node = self
    try:
        while line is None:
            _node = next(_node.get_children())
            line = _node.lineno
    except StopIteration:
        _node = self.parent
        while _node and line is None:
            line = _node.lineno
            _node = _node.parent
    return line