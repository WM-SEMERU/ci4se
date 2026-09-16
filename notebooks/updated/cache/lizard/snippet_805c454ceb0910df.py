def mktz(zone=None):
    if zone is None:
        zone = tzlocal.get_localzone().zone
    zone = six.u(zone)
    tz = dateutil.tz.gettz(zone)
    if not tz:
        raise TimezoneError('Timezone "%s" can not be read' % zone)
    if not hasattr(tz, 'zone'):
        tz.zone = zone
        for p in dateutil.tz.TZPATHS:
            if zone.startswith(p):
                tz.zone = zone[len(p) + 1:]
                break
    return tz