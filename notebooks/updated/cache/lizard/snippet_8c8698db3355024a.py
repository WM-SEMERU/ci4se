def _effective_perm_list_from_iter(self, perm_iter):
    highest_perm_str = self._highest_perm_from_iter(perm_iter)
    return self._equal_or_lower_perm_list(highest_perm_str
        ) if highest_perm_str is not None else None