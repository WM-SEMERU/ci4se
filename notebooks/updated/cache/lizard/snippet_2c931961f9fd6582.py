def get_sample_value(self, name, labels=None):
    if labels is None:
        labels = {}
    for metric in self.collect():
        for s in metric.samples:
            if s.name == name and s.labels == labels:
                return s.value
    return None