def _addSexSpecificity(self, subject_id, sex):
    self.graph.addTriple(subject_id, self.globaltt['has_sex_specificty'], sex)