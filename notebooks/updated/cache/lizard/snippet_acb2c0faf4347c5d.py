def get_key_value_pairs(self, subsystem, filename):
    assert subsystem in self
    return util.read_key_value_pairs_from_file(self.per_subsystem[subsystem
        ], subsystem + '.' + filename)