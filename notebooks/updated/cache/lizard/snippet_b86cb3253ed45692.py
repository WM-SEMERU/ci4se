def _recurse_find_trace(self, structure, item, trace=[]):
    try:
        i = structure.index(item)
    except ValueError:
        for j, substructure in enumerate(structure):
            if isinstance(substructure, list):
                return self._recurse_find_trace(substructure, item, trace + [j]
                    )
    else:
        return trace + [i]