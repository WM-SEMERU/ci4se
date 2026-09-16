def create(login, password, password_hashed=False, machine_account=False):
    ret = 'unchanged'
    if password_hashed:
        password_hash = password.upper()
        password = ''
    else:
        password_hash = generate_nt_hash(password)
    if login not in list_users(False):
        res = __salt__['cmd.run_all'](cmd=
            'pdbedit --create --user {login} -t {machine}'.format(login=
            _quote_args(login), machine='--machine' if machine_account else
            ''), stdin="""{password}
{password}
""".format(password=password))
        if res['retcode'] > 0:
            return {login: res['stderr'] if 'stderr' in res else res['stdout']}
        ret = 'created'
    user = get_user(login, True)
    if user['nt hash'] != password_hash:
        res = __salt__['cmd.run_all'](
            'pdbedit --modify --user {login} --set-nt-hash={nthash}'.format
            (login=_quote_args(login), nthash=_quote_args(password_hash)))
        if res['retcode'] > 0:
            return {login: res['stderr'] if 'stderr' in res else res['stdout']}
        if ret != 'created':
            ret = 'updated'
    return {login: ret}