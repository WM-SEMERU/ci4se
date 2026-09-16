def find_wells_without_curve(self, mnemonic, alias=None):
    return Project([w for w in self if w.get_curve(mnemonic, alias=alias) is
        None])