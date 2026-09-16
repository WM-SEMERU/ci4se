def copy(self, deep=True):
    from copy import copy, deepcopy
    if deep:
        return deepcopy(self)
    else:
        return copy(self)