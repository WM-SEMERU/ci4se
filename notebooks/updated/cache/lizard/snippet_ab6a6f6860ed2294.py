def simple_write(filename, group, times, features, properties=None, item=
    'item', mode='a'):
    write(filename, group, [item], [times], [features], mode=mode,
        properties=[properties] if properties is not None else None)