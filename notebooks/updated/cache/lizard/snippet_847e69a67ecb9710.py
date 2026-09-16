def get_default_padding(self):
    high = 1024 * 10 + self.size // 100
    low = 1024 + self.size // 1000
    if self.padding >= 0:
        if self.padding > high:
            return low
        return self.padding
    else:
        return low