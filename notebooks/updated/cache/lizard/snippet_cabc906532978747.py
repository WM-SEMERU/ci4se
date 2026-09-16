def symmetric_difference_update(self, other):
    r
    other = self._as_multiset(other)
    elements = set(self.distinct_elements()) | set(other.distinct_elements())
    for element in elements:
        multiplicity = self[element]
        other_count = other[element]
        self[element] = (multiplicity - other_count if multiplicity >
            other_count else other_count - multiplicity)