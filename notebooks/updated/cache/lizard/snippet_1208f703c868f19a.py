def parse_input(self, **kwargs):
    super().parse_input(**kwargs)
    self.fn = os.path.join(os.getcwd(), 'built_peptide_table.txt')
    if self.genecentric:
        self.lookuptype = 'peptidegenecentrictable'
    elif self.noncentric:
        self.genecentric = 'plain'
        self.lookuptype = 'peptidetableplain'