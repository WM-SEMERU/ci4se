def prep_jid(nocache=False, passed_jid=None, recurse_count=0):
    if recurse_count >= 5:
        err = 'prep_jid could not store a jid after {0} tries.'.format(
            recurse_count)
        log.error(err)
        raise salt.exceptions.SaltCacheError(err)
    if passed_jid is None:
        jid = salt.utils.jid.gen_jid(__opts__)
    else:
        jid = passed_jid
    jid_dir = salt.utils.jid.jid_dir(jid, _job_dir(), __opts__['hash_type'])
    if not os.path.isdir(jid_dir):
        try:
            os.makedirs(jid_dir)
        except OSError:
            time.sleep(0.1)
            if passed_jid is None:
                return prep_jid(nocache=nocache, recurse_count=
                    recurse_count + 1)
    try:
        with salt.utils.files.fopen(os.path.join(jid_dir, 'jid'), 'wb+'
            ) as fn_:
            fn_.write(salt.utils.stringutils.to_bytes(jid))
        if nocache:
            with salt.utils.files.fopen(os.path.join(jid_dir, 'nocache'), 'wb+'
                ):
                pass
    except IOError:
        log.warning('Could not write out jid file for job %s. Retrying.', jid)
        time.sleep(0.1)
        return prep_jid(passed_jid=jid, nocache=nocache, recurse_count=
            recurse_count + 1)
    return jid