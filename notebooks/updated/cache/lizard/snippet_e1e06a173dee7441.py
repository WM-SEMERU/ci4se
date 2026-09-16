def first_delayed(self):
    entries = self.delayed.zrange(0, 0, withscores=True)
    return entries[0] if entries else None