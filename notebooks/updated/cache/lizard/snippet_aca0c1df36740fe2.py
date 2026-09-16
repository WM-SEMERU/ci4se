def counter(group, counter, amount=1, err=None):
    if not err:
        err = _err
    err('reporter:counter:%s,%s,%s\n' % (group, counter, str(amount)))