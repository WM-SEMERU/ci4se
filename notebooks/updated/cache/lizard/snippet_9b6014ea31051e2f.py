def make_table(self):
    num_records = int(np.sum([(1) for frame in self.timeseries]))
    dtype = [('frame', float), ('time', float), ('ligand atom id', int), (
        'ligand atom name', '|U4'), ('distance', float), ('resid', int), (
        'resname', '|U4'), ('segid', '|U8')]
    out = np.empty((num_records,), dtype=dtype)
    cursor = 0
    for contact in self.timeseries:
        out[cursor] = (contact.frame, contact.time, contact.ligandatomid,
            contact.ligandatomname, contact.distance, contact.resid,
            contact.resname, contact.segid)
        cursor += 1
    return out.view(np.recarray)