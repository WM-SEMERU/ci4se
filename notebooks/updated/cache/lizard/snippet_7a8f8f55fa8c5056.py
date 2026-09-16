def find_tokens(self, q):
    found_me = []
    if hasattr(self, 'location'):
        if self.location.contains(q):
            found_me = [self]
    elif self._found_by(q):
        found_me = [self]
    cs = [n.find_tokens(q) for n in self._children()]
    return found_me + list(itertools.chain(*cs))