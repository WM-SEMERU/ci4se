def datetime_to_synergy(time_qualifier, dt):
    if time_qualifier == QUALIFIER_HOURLY:
        date_format = SYNERGY_HOURLY_PATTERN
    elif time_qualifier == QUALIFIER_DAILY:
        date_format = SYNERGY_DAILY_PATTERN
    elif time_qualifier == QUALIFIER_MONTHLY:
        date_format = SYNERGY_MONTHLY_PATTERN
    elif time_qualifier == QUALIFIER_YEARLY:
        date_format = SYNERGY_YEARLY_PATTERN
    elif time_qualifier == QUALIFIER_REAL_TIME:
        date_format = SYNERGY_SESSION_PATTERN
    else:
        raise ValueError('unknown time qualifier: {0}'.format(time_qualifier))
    return dt.strftime(date_format)