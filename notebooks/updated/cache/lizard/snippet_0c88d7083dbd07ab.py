def process(self, candidates):
    return sorted(candidates, key=attrgetter('score'), reverse=self.reverse)