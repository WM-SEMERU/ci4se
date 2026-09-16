def parse(self, generator):
    gen = iter(generator)
    for line in gen:
        block = {}
        for rule in self.rules:
            if rule[0](line):
                block = rule[1](line, gen)
                break
        yield block