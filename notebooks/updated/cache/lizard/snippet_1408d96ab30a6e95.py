def displ_iter(self, g_nums, ats_1, ats_2, invalid_error=False):
    from .utils import pack_tups
    if _DEBUG:
        print('g_nums = {0}'.format(g_nums))
        print('ats_1 = {0}'.format(ats_1))
        print('ats_2 = {0}'.format(ats_2))
    arglist = self._none_subst(g_nums, ats_1, ats_2)
    tups = pack_tups(*arglist)
    if _DEBUG:
        print(tups)
    for tup in tups:
        yield self._iter_return(tup, self.displ_single, invalid_error)