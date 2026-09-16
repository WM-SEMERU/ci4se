def get_highest_perm_str(self, subj_str):
    pres_perm_set = self._present_perm_set_for_subj(self._perm_dict, subj_str)
    return None if not pres_perm_set else self._highest_perm_from_iter(
        pres_perm_set)