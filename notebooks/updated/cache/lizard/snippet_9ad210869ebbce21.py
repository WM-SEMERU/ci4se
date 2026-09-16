def run(self):
    i = 0
    operation_count = int(self._parameters['operationcount'])
    while i < operation_count:
        i += 1
        weight = random.uniform(0, self._total_weight)
        for j in range(len(self._weights)):
            if weight <= self._weights[j]:
                do_operation(self._database, self._keys, self._parameters[
                    'table'], self._operations[j], self._latencies_ms)
                break