def get_d1nts(self):
    data = []
    ntdata = cx.namedtuple('NtPrt', 'D1 NS dcnt depth GO name')
    namespace = None
    for ntlet in sorted(self.goone2ntletter.values(), key=lambda nt: [nt.
        goobj.namespace, -1 * nt.dcnt, nt.D1]):
        goobj = ntlet.goobj
        goid = goobj.id
        assert len(goobj.parents) == 1
        if namespace != goobj.namespace:
            namespace = goobj.namespace
            ntns = self.ns2nt[namespace]
            pobj = ntns.goobj
            ns2 = self.str2ns[goobj.namespace]
            data.append(ntdata._make([' ', ns2, ntns.dcnt, pobj.depth, pobj
                .id, pobj.name]))
        data.append(ntdata._make([ntlet.D1, self.str2ns[namespace], ntlet.
            dcnt, goobj.depth, goid, goobj.name]))
    return data