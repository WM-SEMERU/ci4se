def subrouters(self):
    yield from filter(lambda mw: isinstance(mw.func, Router), self.mw_list)