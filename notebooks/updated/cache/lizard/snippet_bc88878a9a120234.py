def evaluator(self, candidates, args):
    fitness = []
    if self._use_ants:
        for candidate in candidates:
            total = 0
            for c in candidate:
                total += c.value
            fitness.append(total)
    else:
        for candidate in candidates:
            total_value = 0
            total_weight = 0
            for c, i in zip(candidate, self.items):
                total_weight += c * i[0]
                total_value += c * i[1]
            if total_weight > self.capacity:
                fitness.append(self.capacity - total_weight)
            else:
                fitness.append(total_value)
    return fitness