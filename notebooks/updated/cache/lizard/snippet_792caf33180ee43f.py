def get_grp2codes(self):
    grp2codes = cx.defaultdict(set)
    for code, ntd in self.code2nt.items():
        grp2codes[ntd.group].add(code)
    return dict(grp2codes)