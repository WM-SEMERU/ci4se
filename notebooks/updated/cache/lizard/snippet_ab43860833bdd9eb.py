def stats(self):
    data = Counter()
    for name, value, aggregated in self.raw:
        if aggregated:
            data['%s.max' % name] = max(data['%s.max' % name], value)
            data['%s.total' % name] += value
        else:
            data[name] = value
    return sorted(data.items())