def set_decdel_rts(self):
    lnr = max(self.rows2skip(','), self.rows2skip('.')) + 1
    if self.cnt > EQUAL_CNT_REQ:
        raise PatternError('Did not find ' + str(EQUAL_CNT_REQ) +
            ' data rows with equal data pattern in file: ' + self.fn)
    elif self.cnt < EQUAL_CNT_REQ:
        raise PatternError('Less than', str(EQUAL_CNT_REQ) + 'data rows in',
            self.fn + '?', """
Try lower the EQUAL_CNT_REQ""")
    if self.matches_p[lnr] <= self.matches_c[lnr]:
        self.decdel = '.'
        self.datrx = DATPRX
    else:
        self.decdel = ','
        self.datrx = DATCRX
    self.rts = self.rows2skip(self.decdel)