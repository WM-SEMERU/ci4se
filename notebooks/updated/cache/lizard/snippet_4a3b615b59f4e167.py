def _bool_list(self, k=None):
    n = len(self.func_list)
    if k is None:
        bool_list = [True] * n
    elif isinstance(k, (int, np.integer)):
        bool_list = [False] * n
        bool_list[k] = True
    else:
        bool_list = [False] * n
        for i, k_i in enumerate(k):
            if k_i is not False:
                if k_i is True:
                    bool_list[i] = True
                elif k_i < n:
                    bool_list[k_i] = True
                else:
                    raise ValueError(
                        'k as set by %s is not convertable in a bool string!' %
                        k)
    if self._foreground_shear is True:
        bool_list[self._foreground_shear_idex] = False
    return bool_list