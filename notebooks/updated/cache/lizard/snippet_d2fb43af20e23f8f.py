def _none_subst(self, *args):
    import numpy as np
    arglist = [a for a in args]
    none_found = False
    none_vals = list(map(lambda e: isinstance(e, type(None)), arglist))
    if np.count_nonzero(none_vals) > 1:
        raise ValueError("Multiple 'None' values [indices {0}] not supported"
            .format(tuple(np.nonzero(none_vals)[0])))
    elif np.count_nonzero(none_vals) == 1:
        if not all(np.equal(list(map(np.iterable, arglist)), list(map(lambda
            e: isinstance(e, str), arglist)))):
            raise ValueError(
                "'None' as parameter invalid with non-str iterables")
        none_found = True
        none_loc = np.nonzero(none_vals)[0][0]
        arglist[none_loc] = range(self.num_geoms if none_loc == 0 else self
            .num_atoms)
    return arglist