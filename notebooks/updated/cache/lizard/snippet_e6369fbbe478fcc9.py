def texkeys2marc(self, key, value):
    result = []
    values = force_list(value)
    if values:
        value = values[0]
        result.append({'9': 'INSPIRETeX', 'a': value})
        for value in values[1:]:
            result.append({'9': 'INSPIRETeX', 'z': value})
    return result