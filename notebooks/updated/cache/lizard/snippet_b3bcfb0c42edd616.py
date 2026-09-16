def count(self):
    return self.mapPartitions(lambda p: [sum(1 for _ in p)]).reduce(operator
        .add)