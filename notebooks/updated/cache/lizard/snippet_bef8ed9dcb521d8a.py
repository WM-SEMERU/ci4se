def to_json(self):
    data = dict()
    for key, value in self.__dict__.items():
        if value:
            if hasattr(value, 'to_dict'):
                data[key] = value.to_dict()
            elif isinstance(value, datetime):
                data[key] = value.strftime('%Y-%m-%d %H:%M:%S')
            else:
                data[key] = value
    return json.dumps(data)