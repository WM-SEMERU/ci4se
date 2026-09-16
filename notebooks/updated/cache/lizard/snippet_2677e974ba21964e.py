def _populate_small_table(self, trs):
    for tr in trs:
        tds = tr.select('td')
        cs = Course(title=text(tds[0]), followed=parsebool(tds[1]))
        followed = cs['followed']
        cs['result'] = parsefloat(tds[2]) if followed else None
        cs['jury'] = parsefloat(tds[3]) if followed else None
        cs['session'] = text(tds[4]) if followed else None
        self.append(cs)