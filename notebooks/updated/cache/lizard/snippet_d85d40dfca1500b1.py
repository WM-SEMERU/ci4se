def convert_idx_to_name(self, y, lens):
    y = [[self.id2label[idx] for idx in row[:l]] for row, l in zip(y, lens)]
    return y