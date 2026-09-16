def make_d2p_id(self):
    attributes = [self.onset, self.frequency]
    assoc_id = self.make_association_id(self.definedby, self.disease_id,
        self.rel, self.phenotype_id, attributes)
    return assoc_id