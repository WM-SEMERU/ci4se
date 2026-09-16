def Parse(self, stat, file_object, knowledge_base):
    _, _ = stat, knowledge_base
    users = {}
    wtmp = file_object.read()
    while wtmp:
        try:
            record = UtmpStruct(wtmp)
        except utils.ParsingError:
            break
        wtmp = wtmp[record.size:]
        if record.ut_type != 7:
            continue
        record.user = record.user.split(b'\x00', 1)[0]
        try:
            users[record.user] = max(users[record.user], record.sec, 0)
        except KeyError:
            users[record.user] = record.sec
    for user, last_login in iteritems(users):
        yield rdf_client.User(username=utils.SmartUnicode(user), last_logon
            =last_login * 1000000)