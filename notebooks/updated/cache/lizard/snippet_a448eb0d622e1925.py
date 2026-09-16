def compute_dr_wrt(self, wrt):
    if wrt is self:
        return sp.eye(self.x.size, self.x.size)
    return None