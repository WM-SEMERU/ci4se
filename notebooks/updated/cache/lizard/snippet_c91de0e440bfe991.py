def descendants(self, typename):
    xs = []
    for child in self._hier[typename][1]:
        xs.append(child)
        xs.extend(self.descendants(child))
    return xs