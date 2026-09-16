def deserialize(cls, v, bind_client=None):
    if v is None:
        return None
    az_classes = {'heartrate': HeartrateActivityZone, 'power':
        PowerActivityZone, 'pace': PaceActivityZone}
    try:
        clazz = az_classes[v['type']]
    except KeyError:
        raise ValueError('Unsupported activity zone type: {0}'.format(v[
            'type']))
    else:
        o = clazz(bind_client=bind_client)
        o.from_dict(v)
        return o