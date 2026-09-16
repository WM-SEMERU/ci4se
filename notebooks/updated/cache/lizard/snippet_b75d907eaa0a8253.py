def metric(self, name, filter_=None, description=''):
    return Metric(name, filter_, client=self, description=description)