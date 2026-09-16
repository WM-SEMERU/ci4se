def micro_indices(self):
    return tuple(sorted(idx for part in self.partition for idx in part))