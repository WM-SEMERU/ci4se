def geom_iter(self, g_nums):
    from .utils import pack_tups
    vals = pack_tups(g_nums)
    for val in vals:
        yield self.geom_single(val[0])