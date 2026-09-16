def update(self):
    stats = self.get_init_value()
    if self.input_method == 'local':
        stats = cpu_percent.get(percpu=True)
    else:
        pass
    self.stats = stats
    return self.stats