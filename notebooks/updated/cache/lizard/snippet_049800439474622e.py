def state_pop(self):
    super(Composite, self).state_pop()
    for gen in self.generators:
        gen.state_pop()