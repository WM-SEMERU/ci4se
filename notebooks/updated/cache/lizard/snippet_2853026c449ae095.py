def id_exists(ids, mods, test=None, queue=False, **kwargs):
    ids = salt.utils.args.split_input(ids)
    ids = set(ids)
    sls_ids = set(x['__id__'] for x in show_low_sls(mods, test=test, queue=
        queue, **kwargs))
    return ids.issubset(sls_ids)