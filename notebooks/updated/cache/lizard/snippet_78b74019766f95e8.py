def in_zstack(self, s, c, t):
    if self.series == s and self.channel == c and self.timepoint == t:
        return True
    return False