def get_mark(self, mark_id):
    if mark_id in self.idx:
        return Cmarkable(self.idx[mark_id], self.type)
    else:
        return None