def update_slice(self, blob):
    nexpand, ncontract = blob['nexpand'], blob['ncontract']
    self.scale *= nexpand / (2.0 * ncontract)