def isdisjoint(self, other):
    r
    if isinstance(other, _sequence_types + (BaseMultiset,)):
        pass
    elif not isinstance(other, Container):
        other = self._as_multiset(other)
    return all(element not in other for element in self._elements.keys())