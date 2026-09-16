def reset(self, dim):
    self.dim = dim
    for child_hash in self.child_hashes:
        child_hash['hash'].reset(dim)
        child_hash['bucket_keys'] = {}