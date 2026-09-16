def all_to_annot(self, annot, names=['TPd', 'TPs', 'FP', 'FN']):
    self.to_annot(annot, 'tp_det', names[0])
    self.to_annot(annot, 'tp_std', names[1])
    self.to_annot(annot, 'fp', names[2])
    self.to_annot(annot, 'fn', names[3])