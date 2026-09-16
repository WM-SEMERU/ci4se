def format_csv(self, delim=',', qu='"'):
    res = qu + self.name + qu + delim
    if self.data:
        for d in self.data:
            res += qu + str(d) + qu + delim
    return res + '\n'