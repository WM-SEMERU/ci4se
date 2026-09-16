def reentrancies(self):
    entrancies = defaultdict(int)
    entrancies[self.top] += 1
    for t in self.edges():
        entrancies[t.target] += 1
    return dict((v, cnt - 1) for v, cnt in entrancies.items() if cnt >= 2)