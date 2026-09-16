def get(self):
    model = self.oracle.compute()
    if model:
        if self.htype == 'rc2':
            self.hset = filter(lambda v: v > 0, model)
        else:
            self.hset = model
        return list(map(lambda vid: self.idpool.id2obj[vid], self.hset))