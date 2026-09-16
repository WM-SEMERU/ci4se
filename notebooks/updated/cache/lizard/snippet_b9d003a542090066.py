def alpha(self, a=None):
    if a is not None:
        self.GetProperty().SetOpacity(a)
        return self
    else:
        return self.GetProperty().GetOpacity()