def is_up(coordinate, current_time):
    cfht.date = current_time.iso.replace('-', '/')
    cfht.horizon = math.radians(-7)
    sun.compute(cfht)
    sun_rise = Time(str(sun.rise_time).replace('/', '-'))
    sun_set = Time(str(sun.set_time).replace('/', '-'))
    if current_time < sun_set or current_time > sun_rise:
        return False
    fb._ra = coordinate.ra.radian
    fb._dec = coordinate.dec.radian
    cfht.horizon = math.radians(40)
    fb.compute(cfht)
    fb_rise_time = Time(str(fb.rise_time).replace('/', '-'))
    fb_set_time = Time(str(fb.set_time).replace('/', '-'))
    if (current_time > fb_set_time > fb_set_time or fb_rise_time >
        current_time > fb_set_time):
        return False
    return True