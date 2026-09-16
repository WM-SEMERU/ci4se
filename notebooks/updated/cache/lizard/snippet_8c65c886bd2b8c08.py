def kadd(self, key, value):
    for item in self:
        try:
            item[key].add(value)
        except KeyError:
            item[key] = value
        except AttributeError:
            item[key] = set([item[key], value])