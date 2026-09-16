def _init_edges(self, dst_srcs_list):
    from goatools.gosubdag.go_paths import get_paths_goobjs, paths2edges
    edges_all = set()
    goid_all = set()
    go2obj = self.go2obj
    for dst, srcs in dst_srcs_list:
        go2obj_srcs = {}
        for goid in srcs:
            go2obj_srcs[goid] = go2obj[goid]
        go_paths, go_all = get_paths_goobjs(go2obj_srcs.values(), go_top=
            dst, go2obj=go2obj)
        edges_all |= paths2edges(go_paths)
        goid_all |= go_all
    self.edges = [(a.id, b.id) for a, b in edges_all]
    self.goid_all = goid_all