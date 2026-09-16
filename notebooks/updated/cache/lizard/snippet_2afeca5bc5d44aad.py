def compute(self, config, budget, **kwargs):
    res = numpy.clip(config['x'] + numpy.random.randn() / budget, config[
        'x'] / 2, 1.5 * config['x'])
    time.sleep(self.sleep_interval)
    return {'loss': float(res), 'info': res}