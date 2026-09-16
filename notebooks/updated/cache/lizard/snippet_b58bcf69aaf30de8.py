def filter(name, filter_name, filter_options=None, terms=None, prepend=True,
    pillar_key='acl', pillarenv=None, saltenv=None, merge_pillar=False,
    only_lower_merge=False, revision_id=None, revision_no=None,
    revision_date=True, revision_date_format='%Y/%m/%d', test=False, commit
    =True, debug=False):
    ret = salt.utils.napalm.default_ret(name)
    test = __opts__['test'] or test
    if not filter_options:
        filter_options = []
    if not terms:
        terms = []
    loaded = __salt__['netacl.load_filter_config'](filter_name,
        filter_options=filter_options, terms=terms, prepend=prepend,
        pillar_key=pillar_key, pillarenv=pillarenv, saltenv=saltenv,
        merge_pillar=merge_pillar, only_lower_merge=only_lower_merge,
        revision_id=revision_id if revision_id else name, revision_no=
        revision_no, revision_date=revision_date, revision_date_format=
        revision_date_format, test=test, commit=commit, debug=debug)
    return salt.utils.napalm.loaded_ret(ret, loaded, test, debug)