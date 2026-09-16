def group_factory(bridge, number, name, led_type):
    if led_type in [RGBW, BRIDGE_LED]:
        return RgbwGroup(bridge, number, name, led_type)
    elif led_type == RGBWW:
        return RgbwwGroup(bridge, number, name)
    elif led_type == WHITE:
        return WhiteGroup(bridge, number, name)
    elif led_type == DIMMER:
        return DimmerGroup(bridge, number, name)
    elif led_type == WRGB:
        return WrgbGroup(bridge, number, name)
    else:
        raise ValueError('Invalid LED type: %s', led_type)