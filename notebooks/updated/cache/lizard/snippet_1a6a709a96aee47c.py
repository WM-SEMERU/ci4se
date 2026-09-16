def add_net16string(self, string):
    if len(string) >= 1 << 16:
        raise ValueError('string too long')
    return self.add_net16int(len(string)).add(string)