def humanFriendly(self, time_zone='', include_day=True, include_time=True):
    zeroHourPattern = re.compile('\\s0\\d:')
    title = 'Timezone input for labDT.humanFriendly'
    human_format = ''
    if include_day:
        human_format += '%A, '
    human_format += '%B %d, %Y'
    if include_time:
        human_format += ' %I:%M%p %Z'
    get_tz = get_localzone()
    if time_zone:
        try:
            get_tz = tz.gettz(time_zone)
        except:
            raise ValueError(
                """%s is not a valid timezone format. Try:
for tz in pytz.all_timezones:
  print tz"""
                 % title)
    dtLocal = self.astimezone(get_tz)
    dtString = format(dtLocal, human_format)
    zeroHour = zeroHourPattern.findall(dtString)
    if zeroHour:
        noZero = zeroHour[0].replace(' 0', ' ')
        dtString = zeroHourPattern.sub(noZero, dtString)
    return dtString