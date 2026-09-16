def cardinal(self, to):
    return sum(1 for _ in filter(lambda d: not d.external and d.target in
        to, self.dependencies))