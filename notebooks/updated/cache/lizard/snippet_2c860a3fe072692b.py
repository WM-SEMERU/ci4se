def _get_sortgo(self):
    if 'sortgo' in self.datobj.kws:
        return self.datobj.kws['sortgo']
    return self.datobj.grprdflt.gosubdag.prt_attr['sort'] + '\n'