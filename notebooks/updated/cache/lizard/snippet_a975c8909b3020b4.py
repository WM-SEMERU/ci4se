def contributor_director(**kwargs):
    if kwargs.get('qualifier') in ETD_MS_CONTRIBUTOR_EXPANSION:
        return ETD_MSContributor(role=ETD_MS_CONTRIBUTOR_EXPANSION[kwargs.
            get('qualifier')], **kwargs)
    else:
        return None