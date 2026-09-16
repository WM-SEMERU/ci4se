def as_bin(self, as_spendable=False):
    f = io.BytesIO()
    self.stream(f, as_spendable=as_spendable)
    return f.getvalue()