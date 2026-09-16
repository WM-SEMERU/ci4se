def save_load(jid, clear_load, minions=None, recurse_count=0):
    if recurse_count >= 5:
        err = ('save_load could not write job cache file after {0} retries.'
            .format(recurse_count))
        log.error(err)
        raise salt.exceptions.SaltCacheError(err)
    jid_dir = salt.utils.jid.jid_dir(jid, _job_dir(), __opts__['hash_type'])
    serial = salt.payload.Serial(__opts__)
    try:
        if not os.path.exists(jid_dir):
            os.makedirs(jid_dir)
    except OSError as exc:
        if exc.errno == errno.EEXIST:
            pass
        else:
            raise
    try:
        with salt.utils.files.fopen(os.path.join(jid_dir, LOAD_P), 'w+b'
            ) as wfh:
            serial.dump(clear_load, wfh)
    except IOError as exc:
        log.warning('Could not write job invocation cache file: %s', exc)
        time.sleep(0.1)
        return save_load(jid=jid, clear_load=clear_load, recurse_count=
            recurse_count + 1)
    if 'tgt' in clear_load and clear_load['tgt'] != '':
        if minions is None:
            ckminions = salt.utils.minions.CkMinions(__opts__)
            _res = ckminions.check_minions(clear_load['tgt'], clear_load.
                get('tgt_type', 'glob'))
            minions = _res['minions']
        save_minions(jid, minions)