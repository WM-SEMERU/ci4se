def _create_searchable_typeahead(cls):
    window.destroy_typeahead_tag('#conspect_subconspect_typeahead')
    args = [{'name': name, 'data': [x['name'] for x in cls.
        _get_subconspects(uid)]} for name, uid in conspectus.cosp_id_pairs]
    window.make_multi_searchable_typeahead_tag(
        '#conspect_subconspect_typeahead', *args)