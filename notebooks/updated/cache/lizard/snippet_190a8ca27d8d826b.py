def as_iso8601(self, include_millis=False):
    date = self.__datetime.strftime('%Y-%m-%d')
    time = self.__datetime.strftime('%H:%M:%S')
    if include_millis:
        micros = float(self.__datetime.strftime('%f'))
        millis = '.%03d' % (micros // 1000)
    else:
        millis = ''
    zone = self.__datetime.strftime('%z')
    if float(zone[1:]) == 0.0:
        return '%sT%s%sZ' % (date, time, millis)
    zone_hours = zone[:3]
    zone_mins = zone[3:]
    return '%sT%s%s%s:%s' % (date, time, millis, zone_hours, zone_mins)