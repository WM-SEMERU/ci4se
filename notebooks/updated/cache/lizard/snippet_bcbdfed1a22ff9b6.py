def _aggregate(self, source, aggregators, data, result):
    if data is None:
        return
    if hasattr(aggregators, 'items'):
        for key, value in six.iteritems(aggregators):
            if isinstance(key, tuple):
                key, regex = key
                for dataKey, dataValue in six.iteritems(data):
                    if regex.match(dataKey):
                        result.setdefault(key, {})
                        self._aggregate(source, value, dataValue, result[key])
            elif key == '*':
                for dataKey, dataValue in six.iteritems(data):
                    result.setdefault(dataKey, {})
                    self._aggregate(source, value, dataValue, result[dataKey])
            elif key in data:
                result.setdefault(key, {})
                self._aggregate(source, value, data[key], result[key])
    else:
        for aggregator in aggregators:
            if aggregator.name not in result:
                result[aggregator.name] = aggregator.clone()
            result[aggregator.name].addValue(source, data)