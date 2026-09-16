def update(self, bqm, ignore_info=True):
    self.add_variables_from(bqm.linear, vartype=bqm.vartype)
    self.add_interactions_from(bqm.quadratic, vartype=bqm.vartype)
    self.add_offset(bqm.offset)
    if not ignore_info:
        self.info.update(bqm.info)