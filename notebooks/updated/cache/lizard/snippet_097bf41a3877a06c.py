def __compare_helper(self, other, condition, notimpl_target):
    if not isinstance(other, self.__class__):
        return NotImplemented
    cmp_res = self.__cmp__(other)
    if cmp_res is NotImplemented:
        return notimpl_target
    return condition(cmp_res)