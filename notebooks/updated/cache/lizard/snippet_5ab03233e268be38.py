def runs(self):
    return tuple(_Run(r, self) for r in self._element.r_lst)