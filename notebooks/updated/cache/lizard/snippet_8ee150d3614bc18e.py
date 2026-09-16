def print_computation_log(self, aggregate=False):
    for line in self.computation_log(aggregate):
        print(line)