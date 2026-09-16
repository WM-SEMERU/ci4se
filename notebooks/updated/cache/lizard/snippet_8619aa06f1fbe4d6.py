def multiply(self, number):
    return self.from_list([(x * number) for x in self.to_list()])