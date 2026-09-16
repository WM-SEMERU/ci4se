def scale(self, s=None):
    if s is None:
        return np.array(self.GetScale())
    self.SetScale(s)
    return self