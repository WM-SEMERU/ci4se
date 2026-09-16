def max_csi(self):
    csi = self.contingency_tables['TP'] / (self.contingency_tables['TP'] +
        self.contingency_tables['FN'] + self.contingency_tables['FP'])
    return csi.max()