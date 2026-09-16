def add_metric(self, labels, count_value, sum_value, timestamp=None):
    self.samples.append(Sample(self.name + '_count', dict(zip(self.
        _labelnames, labels)), count_value, timestamp))
    self.samples.append(Sample(self.name + '_sum', dict(zip(self.
        _labelnames, labels)), sum_value, timestamp))