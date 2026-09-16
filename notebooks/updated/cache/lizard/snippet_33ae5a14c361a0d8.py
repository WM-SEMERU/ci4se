def steps(self):

    def _iter(uri, acc):
        acc.appendleft(uri.name if uri.name else '')
        return _iter(uri.parent, acc) if uri.parent else acc
    return _iter(self, acc=deque())