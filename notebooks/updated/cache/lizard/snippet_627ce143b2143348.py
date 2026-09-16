def add(self, idx):
    if (self.leafnode and self.children >= self.max_points_per_region and 
        self.max_depth > 0):
        self.split()
    self.idxs.append(idx)
    if self.leafnode:
        leaf_add = self
    elif self.get_data_x()[idx, self.split_dim] >= self.split_value:
        leaf_add = self.greater.add(idx)
    else:
        leaf_add = self.lower.add(idx)
    self.update_max_progress()
    self.children = self.children + 1
    return leaf_add