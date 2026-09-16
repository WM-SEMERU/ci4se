def _check_time_format(self, labels, values):
    for label, value in zip(labels, values):
        if value == '*':
            continue
        if label == 'day_of_week':
            if isinstance(value, string_types):
                if value not in ORDER_WEEK:
                    raise ParseError(
                        "'%s' is not day of the week. character is the only '%s'"
                         % (value, ', '.join(ORDER_WEEK)))
            elif not isinstance(value, int):
                raise TypeError("'%s' is not an int" % value)
        if label in ['year', 'month', 'day', 'num_of_week']:
            if not isinstance(value, int):
                raise TypeError("'%s' is not an int" % value)
        if isinstance(value, int):
            start, end = TIME_INFO[label]
            if not start <= value <= end:
                raise PeriodRangeError(
                    "'%d' is outside the scope of the period '%s' range: '%d' to '%d'"
                     % (value, label, start, end))