def EnumerateUsersFromClient(args):
    del args
    users = _ParseWtmp()
    for user, last_login in iteritems(users):
        username, _ = user.split(b'\x00', 1)
        username = username.decode('utf-8')
        if username:
            if last_login < 0:
                last_login = 0
            result = rdf_client.User(username=username, last_logon=
                last_login * 1000000)
            try:
                pwdict = pwd.getpwnam(username)
                result.homedir = utils.SmartUnicode(pwdict.pw_dir)
                result.full_name = utils.SmartUnicode(pwdict.pw_gecos)
                result.uid = pwdict.pw_uid
                result.gid = pwdict.pw_gid
                result.shell = utils.SmartUnicode(pwdict.pw_shell)
            except KeyError:
                pass
            yield result