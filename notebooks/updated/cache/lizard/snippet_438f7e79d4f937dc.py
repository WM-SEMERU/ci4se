def rsub(self, items):
    ignore = self._seen
    seen = set()
    add = seen.add
    items = [i for i in items if i not in ignore and i not in seen and not
        add(i)]
    return self._fromargs(seen, items)