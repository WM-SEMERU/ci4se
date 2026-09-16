def get_ordered_types(self):
    types = self.get_types()
    types_arr = np.array(types)
    poss = [self.chrPos, self.startPos, self.stopPos]
    if self.strandPos is not None:
        poss.append(self.strandPos)
    if self.otherPos:
        for o in self.otherPos:
            poss.append(o[0])
    idx_sort = np.array(poss).argsort()
    return types_arr[idx_sort].tolist()