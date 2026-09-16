def to_reminders(self, ical, label=None, priority=None, tags=None, tail=
    None, sep=' ', postdate=None, posttime=None):
    if not hasattr(ical, 'vevent_list'):
        return ''
    reminders = [self.to_remind(vevent, label, priority, tags, tail, sep,
        postdate, posttime) for vevent in ical.vevent_list]
    return ''.join(reminders)