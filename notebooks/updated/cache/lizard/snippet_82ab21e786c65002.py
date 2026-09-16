def generate_random_table(self):
    table = list(range(0, self.n))
    random.shuffle(table)
    return table