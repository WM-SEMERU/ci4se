def do_p(self, arg):
    try:
        self.message(bdb.safe_repr(self._getval(arg)))
    except Exception:
        pass