def _build_dictionary(self, results):
    foreign = self._foreign_key
    dictionary = {}
    for result in results:
        key = getattr(result.pivot, foreign)
        if key not in dictionary:
            dictionary[key] = []
        dictionary[key].append(result)
    return dictionary