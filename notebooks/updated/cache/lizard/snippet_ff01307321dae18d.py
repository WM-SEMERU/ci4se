def format_time(self, hour_expression, minute_expression, second_expression=''
    ):
    hour = int(hour_expression)
    period = ''
    if self._options.use_24hour_time_format is False:
        period = ' PM' if hour >= 12 else ' AM'
        if hour > 12:
            hour -= 12
    minute = str(int(minute_expression))
    second = ''
    if second_expression is not None and second_expression:
        second = '{}{}'.format(':', str(int(second_expression)).zfill(2))
    return '{0}:{1}{2}{3}'.format(str(hour).zfill(2), minute.zfill(2),
        second, period)