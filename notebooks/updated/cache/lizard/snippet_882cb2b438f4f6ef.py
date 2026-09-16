def generator(self, random, args):
    if self.duplicates:
        max_count = [(self.capacity // item[0]) for item in self.items]
        return [random.randint(0, m) for m in max_count]
    else:
        return [random.choice([0, 1]) for _ in range(len(self.items))]