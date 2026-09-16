def push_theme_to_ckan(catalog, portal_url, apikey, identifier=None, label=None
    ):
    ckan_portal = RemoteCKAN(portal_url, apikey=apikey)
    theme = catalog.get_theme(identifier=identifier, label=label)
    group = map_theme_to_group(theme)
    pushed_group = ckan_portal.call_action('group_create', data_dict=group)
    return pushed_group['name']