def _init_c2ps(self, go_sources, traverse_child):
    if not traverse_child:
        return {}
    c2ps = defaultdict(set)
    goids_seen = set()
    go2obj = self.go2obj
    for goid_src in go_sources:
        goobj_src = go2obj[goid_src]
        if goid_src not in goids_seen:
            self._traverse_child_objs(c2ps, goobj_src, goids_seen)
    return c2ps