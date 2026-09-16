def rvs(self, random_state=None):
    r
    if self.dist is None:
        return self.value
    rs = check_random_state(random_state)
    samples = self.dist.rvs(size=self.shape, random_state=rs)
    samples = self.bounds.clip(samples)
    return samples