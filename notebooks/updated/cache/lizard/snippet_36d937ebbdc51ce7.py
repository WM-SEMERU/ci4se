def segment(self, line):
    line = line.strip().split()
    entry = [self.tok2idx[i] for i in line]
    entry = [config.BOS] + entry + [config.EOS]
    return entry