def en_last(self):
    last_ens = dict()
    for k, l in self.en.items():
        last_ens.update({k: l[-1] if l != [] else None})
    return last_ens