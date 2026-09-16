def copy(self):
    wcnf = WCNF()
    wcnf.nv = self.nv
    wcnf.topw = self.topw
    wcnf.hard = copy.deepcopy(self.hard)
    wcnf.soft = copy.deepcopy(self.soft)
    wcnf.wght = copy.deepcopy(self.wght)
    wcnf.comments = copy.deepcopy(self.comments)
    return wcnf