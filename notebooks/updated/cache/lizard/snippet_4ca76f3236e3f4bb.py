def round(self):
    x, y = self.anchor
    self.anchor = normalizers.normalizeRounding(x
        ), normalizers.normalizeRounding(y)
    x, y = self.bcpIn
    self.bcpIn = normalizers.normalizeRounding(x
        ), normalizers.normalizeRounding(y)
    x, y = self.bcpOut
    self.bcpOut = normalizers.normalizeRounding(x
        ), normalizers.normalizeRounding(y)