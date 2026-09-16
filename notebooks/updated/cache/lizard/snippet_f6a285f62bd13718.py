def render(self, namespace):
    ns = namespace.copy()
    result = []
    for item in namespace[self._items]:
        ns[self._item] = item
        result.append(self._block.render(ns))
    return '\n'.join(result) if result else None