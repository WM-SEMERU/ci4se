def from_meters(cls, meter_x=0.0, meter_y=0.0):
    assert -ORIGIN_SHIFT <= meter_x <= ORIGIN_SHIFT, 'Meter X needs to be a value between -{0} and {0}.'.format(
        ORIGIN_SHIFT)
    assert -ORIGIN_SHIFT <= meter_y <= ORIGIN_SHIFT, 'Meter Y needs to be a value between -{0} and {0}.'.format(
        ORIGIN_SHIFT)
    longitude = meter_x / ORIGIN_SHIFT * 180.0
    latitude = meter_y / ORIGIN_SHIFT * 180.0
    latitude = 180.0 / math.pi * (2 * math.atan(math.exp(latitude * math.pi /
        180.0)) - math.pi / 2.0)
    return cls(latitude=latitude, longitude=longitude)