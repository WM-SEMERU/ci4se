def get_smart_data():
    stats = []
    devlist = DeviceList()
    for dev in devlist.devices:
        stats.append({DEVKEY: str(dev)})
        for attribute in dev.attributes:
            if attribute is None:
                pass
            else:
                attribdict = convert_attribute_to_dict(attribute)
                num = attribdict.pop('num', None)
                try:
                    assert num is not None
                except Exception as e:
                    continue
                stats[-1][num] = attribdict
    return stats