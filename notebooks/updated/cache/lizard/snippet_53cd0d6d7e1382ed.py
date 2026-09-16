def push_slack(self, tokens):
    logger.debug('Pushing slack data: %s' % tokens)
    bus = self.case.buses[tokens['bus_no'] - 1]
    g = Generator(bus)
    g.q_max = tokens['q_max']
    g.q_min = tokens['q_min']
    self.case.generators.append(g)
    bus.type = 'ref'