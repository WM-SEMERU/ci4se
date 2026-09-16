def get_filter_config(platform, filter_name, filter_options=None, terms=
    None, prepend=True, pillar_key='acl', pillarenv=None, saltenv=None,
    merge_pillar=True, only_lower_merge=False, revision_id=None,
    revision_no=None, revision_date=True, revision_date_format='%Y/%m/%d'):
    if not filter_options:
        filter_options = []
    if not terms:
        terms = []
    if merge_pillar and not only_lower_merge:
        acl_pillar_cfg = _get_pillar_cfg(pillar_key, saltenv=saltenv,
            pillarenv=pillarenv)
        filter_pillar_cfg = _lookup_element(acl_pillar_cfg, filter_name)
        filter_options = filter_options or filter_pillar_cfg.pop('options',
            None)
        if filter_pillar_cfg:
            pillar_terms = filter_pillar_cfg.get('terms', [])
            terms = _merge_list_of_dict(terms, pillar_terms, prepend=prepend)
    filters = []
    filters.append({filter_name: {'options': _make_it_list({}, filter_name,
        filter_options), 'terms': terms}})
    return get_policy_config(platform, filters=filters, pillar_key=
        pillar_key, pillarenv=pillarenv, saltenv=saltenv, merge_pillar=
        merge_pillar, only_lower_merge=True, revision_id=revision_id,
        revision_no=revision_no, revision_date=revision_date,
        revision_date_format=revision_date_format)