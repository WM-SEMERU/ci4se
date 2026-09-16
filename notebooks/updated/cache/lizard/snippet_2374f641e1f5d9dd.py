def get_queryset(self):
    query_params = list(self.request.query_params.keys())
    filter_criteria = {}
    exclude_if_address_inactive = []
    if 'include_inactive' in query_params:
        if self.request.query_params['include_inactive'] in ['False',
            'false', False]:
            include_inactive = False
        else:
            include_inactive = True
    else:
        include_inactive = True
    for filter in query_params:
        if filter in ['include_inactive', 'cursor']:
            pass
        elif filter.startswith('details__addresses__'):
            filter_criteria[filter + '__has_key'] = self.request.query_params[
                filter]
            if include_inactive is False:
                exclude_if_address_inactive.append((filter.replace(
                    'details__addresses__', ''), self.request.query_params[
                    filter]))
        else:
            filter_criteria[filter] = self.request.query_params[filter]
    identities = Identity.objects.filter(**filter_criteria)
    if include_inactive is False:
        for identity in identities:
            for param in exclude_if_address_inactive:
                q_key = identity.details['addresses'][param[0]][param[1]]
                if 'inactive' in q_key and q_key['inactive'] in [True,
                    'True', 'true']:
                    identities = identities.exclude(id=identity.id)
    return identities