def long_str(self):
    gs = self.git_str
    if gs == '':
        return self.short_str
    return self.short_str + ' (' + gs + ')'