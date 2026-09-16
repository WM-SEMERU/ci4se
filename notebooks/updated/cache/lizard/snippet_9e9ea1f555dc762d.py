def getDueDate(self):
    tat = self.getMaxTimeAllowed()
    if not tat:
        return None
    start = self.getStartProcessDate()
    if not start:
        return None
    delta = timedelta(minutes=api.to_minutes(**tat))
    end = dt2DT(DT2dt(start) + delta)
    if delta.days == 0:
        return end
    setup = api.get_setup()
    workdays = setup.getWorkdays()
    if workdays == tuple(map(str, range(7))):
        return end
    due_date = end - delta.days
    days = 0
    while days < delta.days:
        due_date += 1
        if str(due_date.asdatetime().weekday()) not in workdays:
            continue
        days += 1
    return due_date