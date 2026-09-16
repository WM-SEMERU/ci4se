def filter(self, sids):
    dic = self.__class__(self.shape_y, self.shape_z)
    for sid in sids:
        try:
            dic[sid] = self[sid]
        except KeyError:
            pass
    return dic