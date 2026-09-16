def get_by_index(self, index):
    try:
        return self[index]
    except KeyError:
        for v in self.get_volumes():
            if v.index == str(index):
                return v
    raise KeyError(index)