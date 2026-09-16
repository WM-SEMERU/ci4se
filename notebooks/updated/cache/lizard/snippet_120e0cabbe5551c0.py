def set_limits(self, low=None, high=None):
    if high is not None:
        if self.high_mark is not None:
            self.high_mark = min(self.high_mark, self.low_mark + high)
        else:
            self.high_mark = self.low_mark + high
    if low is not None:
        if self.high_mark is not None:
            self.low_mark = min(self.high_mark, self.low_mark + low)
        else:
            self.low_mark = self.low_mark + low