def register(self, collector):
    if not isinstance(collector, Collector):
        raise TypeError(
            "Can't register instance, not a valid type of collector")
    if collector.name in self.collectors:
        raise ValueError('Collector already exists or name colision')
    with mutex:
        self.collectors[collector.name] = collector