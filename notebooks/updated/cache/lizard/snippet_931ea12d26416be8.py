def from_dict(cls, data):
    args = []
    if 'id' in data and 'data' in data:
        measurement_class = CanMessage
        args.append('Bus %s: 0x%x' % (data.get('bus', '?'), data['id']))
        args.append(data['data'])
    else:
        measurement_class = cls._class_from_name(data['name'])
        if measurement_class == Measurement:
            args.append(data['name'])
        args.append(data['value'])
    return measurement_class(*args, event=data.get('event', None),
        override_unit=True)