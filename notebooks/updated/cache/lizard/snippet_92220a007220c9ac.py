def fmt_cookies(self, ck):
    cks = {}
    for c in ck.split(';'):
        a = c.split('=')
        if len(a) != 2:
            continue
        cks[a[0].replace(' ', '')] = a[1].replace(' ', '')
    self.cookies = cks