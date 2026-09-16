def to_dict(self):
    data = dict()
    for key, value in self.__dict__.items():
        if value:
            if hasattr(value, 'to_dict'):
                data[key] = value.to_dict()
            else:
                data[key] = value
    return data