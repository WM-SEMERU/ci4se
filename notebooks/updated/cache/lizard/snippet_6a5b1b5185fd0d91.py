def unique_id(self):
    chain = self.ampal_parent.ampal_parent.id
    residue = self.ampal_parent.id
    return chain, residue, self.id