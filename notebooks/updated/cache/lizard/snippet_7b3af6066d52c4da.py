def get_best_auth(self, family, address, dispno, types=(b'MIT-MAGIC-COOKIE-1',)
    ):
    num = str(dispno).encode()
    matches = {}
    for efam, eaddr, enum, ename, edata in self.entries:
        if efam == family and eaddr == address and num == enum:
            matches[ename] = edata
    for t in types:
        try:
            return t, matches[t]
        except KeyError:
            pass
    raise error.XNoAuthError((family, address, dispno))