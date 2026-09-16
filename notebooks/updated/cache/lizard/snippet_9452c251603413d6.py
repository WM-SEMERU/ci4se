def next_level(self):
    if self.levl >= len(self.blop):
        self.levl = None
    while self.levl < len(self.blop) - 1:
        numc = sum([len(self.wstr[w]) for w in self.blop[self.levl + 1:]])
        sumw = sum([(w * len(self.wstr[w])) for w in self.blop[self.levl + 1:]]
            )
        if self.blop[self.levl] > sumw and sumw != 0:
            break
        if numc / float(len(self.blop) - self.levl - 1) > self.sdiv:
            break
        self.levl += 1