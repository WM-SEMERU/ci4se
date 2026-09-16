def median(self):
    mu = self.mean()
    ret_val = math.exp(mu)
    if math.isnan(ret_val):
        ret_val = float('inf')
    return ret_val