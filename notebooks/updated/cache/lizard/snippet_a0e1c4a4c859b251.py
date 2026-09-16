def format(self, record):
    super(CliFormatter, self).format(record)
    localized_time = datetime.datetime.fromtimestamp(record.created)
    terse_time = localized_time.strftime('%H:%M:%S')
    terse_level = record.levelname[0]
    terse_name = record.name.split('.')[-1]
    match = RECORD_LOGGER_RE.match(record.name)
    if match:
        subsys_match = SUBSYSTEM_LOGGER_RE.match(record.name)
        if subsys_match:
            terse_name = '<{subsys}: {id}>'.format(subsys=subsys_match.
                group('subsys'), id=subsys_match.group('id'))
        else:
            terse_name = '<test %s>' % match.group('test_uid')[-5:]
    return '{lvl} {time} {logger} - {msg}'.format(lvl=terse_level, time=
        terse_time, logger=terse_name, msg=record.message)