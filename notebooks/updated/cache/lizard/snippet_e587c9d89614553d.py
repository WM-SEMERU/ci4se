def _parse_rruleset(rruleset):
    if rruleset._rrule[0]._freq == 0:
        return []
    rep = []
    if rruleset._rrule[0]._byweekday and len(rruleset._rrule[0]._byweekday
        ) > 1:
        rep.append('*1')
    elif rruleset._rrule[0]._freq == rrule.DAILY:
        rep.append('*%d' % rruleset._rrule[0]._interval)
    elif rruleset._rrule[0]._freq == rrule.WEEKLY:
        rep.append('*%d' % (7 * rruleset._rrule[0]._interval))
    else:
        return Remind._parse_rdate(rruleset._rrule[0])
    if rruleset._rrule[0]._byweekday and len(rruleset._rrule[0]._byweekday
        ) > 1:
        daynums = set(range(7)) - set(rruleset._rrule[0]._byweekday)
        weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        days = [weekdays[day] for day in daynums]
        rep.append('SKIP OMIT %s' % ' '.join(days))
    if rruleset._rrule[0]._until:
        rep.append(rruleset._rrule[0]._until.strftime('UNTIL %b %d %Y').
            replace(' 0', ' '))
    elif rruleset._rrule[0]._count:
        rep.append(rruleset[-1].strftime('UNTIL %b %d %Y').replace(' 0', ' '))
    return rep